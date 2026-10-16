<!-- theorem-state: {"artifact_id":"ART-8A94C71ECC92","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# A global boundary zigzag competitor with a linear population reserve

**Classification:** proved candidate awaiting promotion; **unreviewed**.
**Level I remains open.**

Baseline `ab6dd3336f9f8d440f2bada76edb32153391cddc`, state
`2026-10-10.audit.234`; independent branch
`research/sol/global-independent-20261011`.

## 1. Statement and global implication

Write `a0=sqrt(3)/2` and `a=pi/(2sqrt(3))`. For every real
`R>=640000`, there exists a unit-separated set in the closed radius-`R` disk
with cardinality at least

\[
\boxed{{\pi R^2\over a_0}+{R\over160000}.}
\tag{1}
\]

More precisely, **every translate** of the triangular lattice, cropped to this
disk, admits the explicitly described boundary replacement gaining at least
`R/160000` points. Translation averaging then supplies (1).

Consequently every global minimum-diameter `n`-point unit-separated source with
`D>1280000` satisfies

\[
\boxed{g_A:=n-1-aD^2\ge {D\over320000}.}
\tag{2}
\]

The implication chain is

```text
simultaneous boundary replacements in a whole lattice disk
  -> a full-source independent competitor with linear extra population
  -> the global-minimizer population reserve (2).
```

The construction does not move a hypothetical minimizer or identify it with a
lattice. It constructs a separate configuration of controlled diameter, then
uses global optimality only for the cardinality comparison. It retains all
labels of a hypothetical source in that comparison. This is a global population
result, not a triangle theorem or a C-II finite-motion theorem.

## 2. One row replacement, including the complete pair ledger

Use the triangular lattice

\[
\Lambda_t=\{t+(j+k/2,ka_0):j,k\in\mathbb Z\}.
\]

Let `y=t_y+ka0>0` be one row height. Suppose an interval `[A,B]`, with integer
endpoints and length `L=B-A`, has these two properties in the disk:

1. `(x,y+1/2)` lies in the disk for every `x in [A,B]`;
2. no retained lattice point of a higher row has horizontal coordinate in
   `(A,B)`.

Delete exactly the row-`y` lattice points whose horizontal coordinates lie in
`[A,B]`. There are at most `L+1` of them, irrespective of translation or row
parity. Set `h=19/20`, and insert

\[
p_i=(A+1+ih,\ y+\eta_i),\qquad
0\le i\le\left\lfloor{L-2\over h}\right\rfloor,
\]

where `eta_i=1/6` for even `i` and `eta_i=1/2` for odd `i`.

All the pair checks are explicit:

- Adjacent inserted points have squared distance
  `h^2+(1/3)^2=3649/3600>1`.
- Nonadjacent inserted points have horizontal separation at least `2h=19/10>1`.
- Every lower lattice row has vertical separation at least
  `a0+1/6>1` from every inserted point.
- Retained points on the same row lie outside `[A,B]`, hence have horizontal
  separation at least one and positive vertical separation.
- Higher retained rows have horizontal coordinates outside `(A,B)`, so have
  horizontal separation at least one and positive vertical separation.
- Inserted points stay in the disk: they are above the positive row `y`, below
  its height `y+1/2`, and at horizontal coordinates in `[A,B]`.

Thus every new-involving lower distance is in fact strict. Old retained pairs
keep their original lower bound. No assertion about a stress or a local
linearization is used.

The net cardinality gain is at least

\[
{L-2\over h}-(L+1)={L-59\over19}.
\tag{3}
\]

For `L>64`, the integer gain is therefore at least one.

## 3. Simultaneously available rows on a shallow circular arc

Set `delta=1/200` and `f(x)=sqrt(R^2-x^2)`. Work only in the upper-right
arc with horizontal coordinate between `delta R/2` and `delta R`.
Choose every lattice row `y` such that

\[
f(\delta R)\le y,
\qquad y+a_0\le f(\delta R/2).
\tag{4}
\]

Define real endpoints and their inward integer roundings by

\[
u_y=\sqrt{R^2-(y+a_0)^2},\qquad
v_y=\sqrt{R^2-(y+1/2)^2},\qquad
A_y=\lceil u_y\rceil,\quad B_y=\lfloor v_y\rfloor.
\tag{5}
\]

For `x in [A_y,B_y]`, the disk top is at least `y+1/2` and at most
`y+a0`. Equality at the left endpoint is harmless because of the one-unit
horizontal guard used by the packet. Thus both hypotheses of Section 2 hold.

Throughout these intervals,

\[
\left|{d\over dz}\sqrt{R^2-z^2}\right|
={z\over\sqrt{R^2-z^2}}
\ge {\sqrt{1-\delta^2}\over\delta}>199.
\]

Since `a0-1/2>1/3`, the mean value theorem and rounding give

\[
v_y-u_y>{199\over3},\qquad
L_y=B_y-A_y>{199\over3}-2={193\over3}>64.
\tag{6}
\]

Each selected row therefore gains at least one point.

The intervals for different rows are disjoint: their corresponding height
intervals `[y+1/2,y+a0]` are disjoint, and `z -> sqrt(R^2-z^2)` is
strictly decreasing here. Integer rounding only shrinks the intervals. Every
packet stays one unit inside each of its interval endpoints. Two packets on
different rows consequently have horizontal separation at least two. The row
replacements are **simultaneously** feasible, and they delete disjoint sets of
old labels. This checks the cross-packet constraints, not just single-row moves.

Let

\[
\Delta=f(\delta R/2)-f(\delta R).
\]

The number `K` of rows satisfying (4), for any vertical lattice translation,
obeys

\[
K\ge {\Delta\over a_0}-2\ge\Delta-2.
\tag{7}
\]

Rationalizing the difference of square roots gives

\[
\Delta
={3\delta^2R/4\over
\sqrt{1-\delta^2/4}+\sqrt{1-\delta^2}}
\ge {3\delta^2R\over8}={3R\over320000}.
\]

For `R>=640000`, equations (7) therefore give

\[
K\ge {3R\over320000}-2\ge {R\over160000}.
\tag{8}
\]

The untouched bulk, the remaining boundary rows, and all the packets form one
unit-separated packing in the original disk. This proves the claimed gain for
every translated lattice crop.

## 4. Averaging and the strict global comparison

Average `|Lambda_t cap B(0,R)|` over one fundamental parallelogram. The mean is
`pi R^2/a0`; some translate has at least that many points. Apply the construction
to that translate and use (8), proving (1).

Now suppose an `n`-point global minimizer has diameter `D>1280000`. For every
`640000<=R<D/2`, (1) supplies a packing of some integer cardinality `N_R` and
diameter at most `2R<D`. If `N_R>=n`, any `n`-point subset contradicts global
optimality. Therefore

\[
n-1\ge N_R\ge {\pi R^2\over a_0}+{R\over160000}.
\]

Take `R` up to `D/2`. The right side is continuous, so (2) follows. This limiting
step preserves the strict smaller-diameter comparison: each individual
competitor used before the limit has diameter strictly below `D`.

The construction proves existence of a separate competitor, with its entire
lower and upper pair ledger checked. It does not assume a source lattice frame,
a supplied train family, stress-weight lower bounds, or any omitted-label bound.

## 5. Why this does not by itself settle Level I

The new reserve is linear in `D`; a source-specific upper estimate
`g_A=o(D)` for normalized triangle-free global minimizers would now suffice.
Such an upper estimate has **not** been proved here.

It cannot hold for arbitrary triangle-free unit-separated sources. Fix any
`0<c<1/320000`. In the construction above choose `R<D/2` sufficiently close
to `D/2` that the resulting count is at least `aD^2+cD`. Then apply
`(x,y)->(x,(1+epsilon)y)` for a sufficiently small positive `epsilon` so
`2R(1+epsilon)<D`. All distances weakly increase, and a distance can remain
one only for a horizontal pair. Thus the new contact graph is a disjoint union
of horizontal paths and is triangle-free. The untouched central lattice region
contains horizontal unit pairs, so the minimum distance is still exactly one.
The cardinality is unchanged and the diameter is still strictly below `D`.

This accompanying **regression** rules out a triangle-free-only `o(D)` upper
bound. A closing bound must use the exact global-minimizer hypotheses. The
construction does not claim its triangle-free deformations are globally optimal.

## 6. Verification, dependency and lifecycle notes

The proof is elementary: triangular-lattice translation averaging, explicit
distance arithmetic, and the mean value theorem. Canonical modules are needed
only for the problem definition and the interpretation of `g_A`; no unpromoted
research theorem is used as a premise.

`research/verify_global_boundary_zigzag_2026_10_11.py` constructs actual packets
at specified rational radii and lattice translates. It checks the selected disk
rows using rational intervals, enumerates every retained-lattice label that
could be within unit distance of a packet label using exact `Q(sqrt(3))`
comparisons, checks packet containment and cross-packet separation, and records
the exact deletion/insertion gain. It does not enumerate the quadratic-size
untouched lattice crop; those unchanged pairs are handled by lattice separation.
The all-radius theorem and translation average are proved above, not inferred
from the finite checks.

This candidate awaits independent audit. It is not a promotion, a Level I
solution, or a source-realized C-II motion. No canonical status file is changed.

The completed finite run checked 154 simultaneous packets across five
radius/translation examples, 15,460 inserted labels, and 155,481 potentially
close retained-lattice pairs. The total net gain was 534 labels. The smallest
tested radius was exactly the claimed threshold `R=640000`; nonintegral
horizontal and vertical translations were included. All five cases passed.

The author's scope review separately checked integer endpoint rounding,
arbitrary lattice translation, upper rows at interval endpoints, neighboring
packet compatibility, and the `R`-to-`D/2` limit. This is a self-review, not
the independent audit required for canonical promotion.

## 7. Exact transport to the existing global population ledgers

The following consequences are conditional on acceptance of (2); they are
algebraic transports of this unreviewed candidate, not new canonical endpoints.
Put `c=1/320000`, `c0=a0/2`, and
`delta_K=pi D^2/4-area(K)>=0` for the full source hull.

In the precise scope where the Target B Section 36 identities hold,

\[
n=R_4+B/2+\chi+t,\qquad
\operatorname{area}(K)=a_0R_4+E+G,
\]

define `Q=c0 B+a0(t+chi-1)`. There is an **exact** identity

\[
Q-(G+E)
=a_0(n-1)-\operatorname{area}(K)
=a_0g_A+\delta_K.
\]

Thus the candidate sharpens the necessary upper shell bound to

\[
\boxed{G+E\le Q-\delta_K-{\sqrt3\over640000}D.}
\tag{11}
\]

In particular, a uniform source-specific lower bound
`G+E>=Q-epsilon D` for any fixed `epsilon<sqrt(3)/640000`
would suffice for contradiction. The stronger old target `G+E>=Q` is no
longer necessary if (2) is promoted. All topology and omitted-vertex terms in
`t+chi-1` remain present. This does not establish the proposed lower bound.

For the canonical Target C Section 67 full-source force-hull population
inequality, retain `N_F` for all labels in `F`, `Z_ext=n-N_F`, and
`delta_F=pi D^2/4-area(F)`. Its proved upper bound is

\[
a_0N_F\le\operatorname{area}(F)+c_0P_F+a_0-E_4.
\]

Substitution, with no population deletion, gives

\[
\boxed{E_4+\delta_F+a_0g_A\le a_0Z_{ext}+c_0P_F,}
\]

and hence the candidate consequence

\[
\boxed{E_4+\delta_F
\le a_0Z_{ext}+c_0P_F-{\sqrt3\over640000}D.}
\tag{12}
\]

Every contact isolate is included in either `N_F` or `Z_ext`. The estimate does
not supply a bound on `Z_ext`, an endpoint, or a capacity surplus. It identifies
the exact new amount that a global boundary/interface argument can spend;
neither (11) nor (12) closes its route by itself.

Sources for the transported identities are
[`target-b/01-jammed-rhombic-branch.md`, Section 36](../targets/target-b/01-jammed-rhombic-branch.md)
and [`target-c/67-rhombus-population-transport-audit.md`](../targets/target-c/67-rhombus-population-transport-audit.md).
