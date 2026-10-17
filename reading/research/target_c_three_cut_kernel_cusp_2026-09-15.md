> Generated reading edition · [exact source](../../research/target_c_three_cut_kernel_cusp_2026-09-15.md) · source SHA-256 `f7e9d15d937288e2b748a1340729603936e0b99ff6c7e9dd8a0766be788c5cb7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e1e85f9e64c0a3e72bdaca94e0cc9e474121cdb0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_three_cut_kernel_cusp_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e679a0e4745d7735cb4f81d50cced66ed85dd850db2c9841404e762693b81178"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — three consecutive cuts isolate the diameter cusp exactly at first order

**Date:** 2026-09-15  
**Status:** proof-only exact structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`, on the good smallest-leaf backbone used by the adjacent triple-small theorem  
**Dependencies:** audited adjacent-pair triple-small budgets; exact laminar finite multishear and interval support; canonical mixed infinitesimal rigidity; canonical maximal-support KKT stress  
**Certificate:** `research/verify_target_c_three_cut_kernel_cusp.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Two cuts leave a phase-mismatch leakage on diameter rows spanning both cuts. Three planar train vectors have an exact linear dependence, so three consecutive cuts can remove that leakage **exactly at first order**.

There exist three consecutive smallest-leaf O-O cuts

$$
\tau_1,\tau_2,\tau_3
$$

on one live complement-dual backbone and a nonzero coefficient vector

$$
c=(c_1,c_2,c_3),
\qquad
\max_j|c_j|=1,
$$

for the shore-oriented unit train vectors `u_j` such that

$$
\boxed{c_1u_1+c_2u_2+c_3u_3=0.}
\tag{KC.1}

For the exact contact-preserving multishear

\[
\theta_j=t c_j,
\tag{KC.2}

all actual diameter rows except a bounded exceptional set have **zero first squared-length derivative exactly**. The exceptional set is the union of the switching rows at the two internal cut boundaries, and satisfies

\[
\boxed{\#H_{exc}<42400+o(1),}
\tag{KC.3}
$$

$$
\boxed{
\sum_{h\in H_{exc}}\beta_h
<{42400\over D}+o(D^{-1})
}
\tag{KC.4}
$$

for a normalized maximal-support KKT stress.

The same three cuts can be chosen with total adjacent projective phase variation

$$
\boxed{
 d_{\mathbb{RP}^1}(u_1,u_2)
 +d_{\mathbb{RP}^1}(u_2,u_3)
 <{42400\over D}+o(D^{-1}).
}
\tag{KC.5}

Moreover the KKT-weighted first derivatives on `H_exc` satisfy the exact balance

\[
\boxed{
\sum_{h\in H_{exc}}
\beta_h {d\over dt}|r_h(t)|^2\Big|_{t=0}=0.
}
\tag{KC.6}

The shear is non-Euclidean, so at least one actual exceptional diameter row has nonzero first derivative. Consequently exactly one of the following holds:

1. **force-visible cusp:** some maximal-support positive-KKT exceptional row has nonzero derivative, in which case positive-KKT exceptional rows occur with both derivative signs;
2. **force-invisible blocker:** every positive-KKT exceptional row has zero derivative, in which case some nonzero exceptional blocker is an active diameter edge outside the canonical maximal KKT support and is therefore universally zero-KKT.

Finally, if the three shore-oriented train directions span the plane, the first-order kernel integrates to an exact local one-parameter finite multishear for which **every nonexceptional diameter row is unchanged exactly**, not merely to first order. Thus in the nonparallel case the entire local finite diameter obstruction is the bounded set `H_exc`.

---

## 1. Average two consecutive internal boundaries at once

Use the notation of the adjacent triple-small theorem. Along the good-leaf backbone

\[
P=(\tau_1,\ldots,\tau_m),
\qquad
m>pD-o(D),
$$

that theorem defines nonnegative internal-boundary costs

$$
T_i=N_i+DB_i+D(q_i+q_{i+1}),
\qquad 1\le i<m,
\tag{KC.7}
$$

and proves

$$
\sum_{i=1}^{m-1}T_i
\le C_*D+o(D)
$$

with

$$
{C_*\over p}<21175.904<21200.
\tag{KC.8}
$$

For a consecutive triple of cuts, use the two-boundary cost

$$
U_i:=T_i+T_{i+1},
\qquad 1\le i\le m-2.
$$

Every `T_j` occurs in at most two `U_i`, so

$$
\sum_{i=1}^{m-2}U_i
\le2\sum_{j=1}^{m-1}T_j.
$$

Since `m>pD-o(D)`, some triple satisfies

$$
U_i<2(21175.904)+o(1)<42400+o(1).
\tag{KC.9}
$$

The companion exact verifier recomputes the parent rational constant and gives

$$
2K=42351.8078\ldots<42400,
$$

leaving more than `48` units of room.

Because every term in `T_i,T_{i+1}` is nonnegative, the chosen triple obeys

$$
N_i+N_{i+1}<42400+o(1),
\tag{KC.10}
$$

$$
D(B_i+B_{i+1})<42400+o(1),
\tag{KC.11}
$$

and

$$
D[(q_i+q_{i+1})+(q_{i+1}+q_{i+2})]
<42400+o(1).
\tag{KC.12}
$$

The projective adjacent gaps are bounded respectively by the two bracketed terms, so (KC.5) follows.

Relabel this chosen triple as `tau_1,tau_2,tau_3`.

---

## 2. Three planar train vectors have an exact shear kernel

Use the shore-oriented unit vectors furnished by the exact laminar multishear theorem for the three chosen cuts. Consider the linear map

$$
L:\mathbb R^3\to\mathbb R^2,
\qquad
L(c)=c_1u_1+c_2u_2+c_3u_3.
$$

Its kernel is nontrivial because the domain has dimension three and the target has dimension two. Choose

$$
0\ne c\in\ker L
$$

and normalize `max |c_j|=1`. This proves (KC.1).

The exact laminar motion

$$
p_v(t)
=p_v+
\sum_{j:v\in S_j}
(R_{c_jt}u_j-u_j)
\tag{KC.13}
$$

preserves every old unit contact exactly for all sufficiently small `t` and preserves strict old noncontacts by continuity.

For an actual diameter row `h`, orient its endpoints by increasing layer index. Its first relative-displacement coefficient is

$$
A_h
=J\sum_{j\in I_h\cap\{1,2,3\}}c_ju_j.
\tag{KC.14}
$$

If the row meets none of the three cuts, `A_h=0`.

If it meets all three cuts, then (KC.1) gives

$$
\boxed{A_h=0.}
\tag{KC.15}
$$

Thus every row of these two nonexceptional types has

$$
{d\over dt}|r_h(t)|^2\Big|_0=2r_h\cdot A_h=0
$$

**exactly**, with no inverse-`D` phase error.

---

## 3. Every remaining row switches at one of the two internal boundaries

Interval support implies that the intersection of a diameter row with the selected triple is a contiguous subset of

$$
\{1,2,3\}.
$$

Besides the empty and full subsets, the only possibilities are

$$
\{1\},\ \{2\},\ \{3\},\ \{1,2\},\ \{2,3\}.
$$

Every one changes incidence across boundary `1|2` or boundary `2|3`. Hence every diameter row with potentially nonzero first derivative lies in

$$
H_{exc}:=H_{sw,1}\cup H_{sw,2}.
\tag{KC.16}
$$

Therefore

$$
\#H_{exc}
\le N_i+N_{i+1}
<42400+o(1),
$$

which is (KC.3).

Choose the canonical maximal-support normalized KKT multiplier. A row that switches across one internal boundary contributes exactly one unit to the corresponding incidence variation; a row supported only on the middle cut may be counted at both boundaries, which is harmless. Hence

$$
\sum_{h\in H_{exc}}\beta_h
\le B_i+B_{i+1}
<{42400\over D}+o(D^{-1}),
$$

proving (KC.4).

---

## 4. KKT stationarity is supported entirely on the finite cusp

For each selected train coordinate, the audited cut resultant is parallel to its train vector:

$$
F_j
:=\sum_h\beta_h\varepsilon_{hj}r_h
=A_ju_j.
$$

Therefore

$$
\sum_h\beta_h\varepsilon_{hj}(r_h\cdot Ju_j)
=F_j\cdot Ju_j
=0.
\tag{KC.17}
$$

Multiply by `c_j`, sum over the three coordinates, and use the exact derivative formula. This gives

$$
\sum_h\beta_h
{d\over dt}|r_h(t)|^2\Big|_0=0.
\tag{KC.18}
$$

Every row outside `H_exc` has zero derivative by Sections 2--3. Thus (KC.18) reduces exactly to (KC.6).

No small-error term survives in the first-order balance.

---

## 5. The exceptional cusp is nontrivial

Suppose every actual diameter row in `H_exc` also had zero first derivative. Then every actual diameter row would have zero first variation under the three-cut shear, while every unit contact has zero first variation because the exact multishear preserves it.

Canonical mixed infinitesimal rigidity would make the shear velocity Euclidean.

But its angular rate on selected train `tau_j` is `c_j`, while every unselected complete train has angular rate zero. In particular the center train `gamma` used to build the backbone crosses the selected leaves and is not one of them, so its rate is zero. A Euclidean rotation has one common angular rate on every train; hence that common rate would be zero. A translation has zero relative train rates as well. Therefore all `c_j` would vanish, contradicting the choice `c!=0`.

So

$$
\boxed{
\exists h\in H_{exc}:\quad
{d\over dt}|r_h(t)|^2\Big|_0\ne0.
}
\tag{KC.19}

---

## 6. Positive-stress sign cusp or universally zero-KKT blocker

The canonical maximal-support KKT stress is positive on exactly the diameter edges in

\[
H_*:=\{h:\beta_h>0\text{ in some normalized KKT stress}\}.
$$

Hence an active diameter row with zero multiplier in this maximal-support stress lies outside `H_*` and is universally zero-KKT.

If some `h in H_exc cap H_*` has nonzero first derivative, then its multiplier is positive. The exact weighted balance (KC.6) and positivity of all multipliers on `H_*` force another force-visible exceptional row with the opposite derivative sign.

If instead every force-visible exceptional row has zero derivative, (KC.19) supplies a nonzero exceptional derivative on an active row outside `H_*`. That row is a universally zero-KKT active diameter constraint.

Thus the obstruction has the exact dichotomy announced above:

```text
finite positive-stress cusp with both first-derivative signs
OR
finite first-order blocker carried by a universally zero-KKT diameter row.
```

This ties the live train-shear obstruction directly to the older canonical force-hull / weak-active-constraint program.

---

## 7. Nonparallel triples integrate to an exact finite cusp

There is an additional finite strengthening when the three shore-oriented train vectors span the plane.

Define

$$
G(\theta_1,\theta_2,\theta_3)
:=\sum_{j=1}^3(R_{\theta_j}u_j-u_j)
\in\mathbb R^2.
\tag{KC.20}
$$

Then

$$
DG(0)[a_1,a_2,a_3]
=J\sum_j a_ju_j.
$$

If `span{u_1,u_2,u_3}=R^2`, this derivative has rank two. The implicit-function theorem therefore makes `G^{-1}(0)` a one-dimensional smooth manifold through the origin. Its tangent space is exactly `ker L`, so it contains a nonconstant local curve

$$
\theta(s),
\qquad
\theta(0)=0,
\qquad
\theta'(0)=c,
\qquad
G(\theta(s))=0.
\tag{KC.21}
$$

Use this angle curve in the exact laminar finite multishear.

- a diameter row meeting none of the selected cuts is unchanged exactly;
- a diameter row meeting all three has exact relative-displacement increment `G(theta(s))=0`, so it is also unchanged exactly;
- every old unit contact is preserved exactly by the multishear theorem;
- all strict old noncontacts and subdiameter pairs remain strict for sufficiently small `s` by finiteness and continuity.

Therefore, in the nonparallel case, **only the bounded exceptional set `H_exc` changes at all** under this genuine finite source motion.

The rank-one/projectively-parallel triple is left as a separate regression. The theorem does not claim an exact nontrivial `G=0` curve there.

---

## 8. Frontier effect

The previous two-cut finite cusp had two defects outside its bounded switching set:

1. spanning diameter rows retained an `O(D^-1)` vector mismatch at first order;
2. at finite amplitude they therefore required a residual global error ledger.

The three-cut kernel removes defect 1 exactly. In the nonparallel case the implicit-function integration removes defect 2 exactly as well.

The remaining live obstruction is now one of two finite source-level objects:

- an ordered positive-stress switching cusp with both signs; or
- a universally zero-KKT active diameter blocker.

The newly proved adjacent switching one-arc theorem can be applied boundary-by-boundary inside `H_exc`. A useful next theorem should either combine the two ordered interfaces into a finite sign classification, or prove a release/exchange move for the universally zero-KKT blocker branch.

**Disposition:** proved proof-only exact three-cut kernel reduction. C-II and Level I remain open.
