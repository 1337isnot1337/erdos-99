> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_primitive_boundary_normal_form_2026-09-09.md) · source SHA-256 `f80e869968f2124eaef2d471998b92c663009bda461525aa249a2abbb6a0475c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E6AF1F800FB5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — primitive post-ZF boundary normal form

**Date:** 2026-09-09  
**Repository base:** PR #118 after loaded hull-contact slack  
**Run type:** exact ledger elimination / structural normal form  
**Target:** Target C, C-II after ZF  
**Depends on:** LH loaded hull-contact slack, ZT/ZU exact post-ZF ledgers, ZK component-slack cancellation  
**External web search:** not used in the proof  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The LH hull-contact refinement lets the post-ZF ledgers be rewritten in primitive geometric variables.

Let

- `m` be the number of consecutive loaded force-hull sides of Euclidean length greater than one;
- `u_B=x_B-m>=0` be the residual outer-walk excess;
- `c_B=e_BB-(q-m)>=0` be the number of loaded-loaded contacts beyond the unit force-hull sides;
- `k=d_H+s_Z`.

Then

$$
\boxed{x_B=m+u_B,}
\tag{PN.1}
$$

$$
\boxed{e_{BB}=q-m+c_B,}
\tag{PN.2}
$$

and ZT gives

$$
\boxed{q=m+u_B+Q+2k.}
\tag{PN.3}
$$

The two main exact cancellations are

$$
\boxed{
c_I+s_C+c_B=m+k-2,}
\tag{PN.4}
$$

and

$$
\boxed{
\sum_r\delta_r+R_I+s_B+k
=6+u_B+Q+2s_C+c_B.}
\tag{PN.5}
$$

Thus the entire post-ZF boundary/contact state can be parameterized without the composite variables `x_B` and `e_BB`.

---

## 1. Derivation of the first cancellation

ZU gives

$$
c_I+e_{BB}+s_C=q-2+k.
\tag{1.1}
$$

Substitute PN.2:

$$
c_I+q-m+c_B+s_C=q-2+k.
$$

Cancel `q` and rearrange:

$$
\boxed{c_I+s_C+c_B=m+k-2.}
$$

This proves PN.4. `square`

Every term on the left is nonnegative, so immediately

$$
\boxed{m+k\ge2.}
\tag{PN.6}
$$

More precisely,

$$
\boxed{
 c_I\le m+k-2,
\quad
 s_C\le m+k-2,
\quad
 c_B\le m+k-2.}
\tag{PN.7}
$$

This is stronger than treating these quantities as unrelated post-ZF currencies. The number of nonunit convex-hull sides and the mixed/diameter defect together pay for every unpinned contact component, every extra pinned-contact stress dimension, and every extra loaded-loaded contact chord.

---

## 2. Derivation of the second cancellation

ZK gives

$$
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
\tag{2.1}
$$

Using PN.2 and PN.3,

$$
\begin{aligned}
e_{BB}
&=q-m+c_B\\
&=(m+u_B+Q+2k)-m+c_B\\
&=u_B+Q+2k+c_B.
\end{aligned}
\tag{2.2}
$$

Substitute into ZK and cancel `2k` from both sides:

$$
\sum_r\delta_r+R_I+s_B+k
=6+u_B+Q+2s_C+c_B.
$$

This is PN.5. `square`

The striking feature is that `m` disappears completely from PN.5. The **count** of missing unit hull sides controls how many interior/stress/chord objects may exist through PN.4, while the **residual depth** `u_B` controls the remaining component-diameter budget through PN.5.

---

## 3. Exact expression for the loaded-boundary degree slack

C35/ZK use

$$
s_B:=3q-e_{BI}-2e_{BB}\ge0.
$$

Substituting PN.2 gives

$$
\boxed{
e_{BI}+2c_B+s_B=q+2m.}
\tag{PN.8}
$$

Thus the contact-degree capacity left after paying the `q-m` unit hull sides is exactly `q+2m`.

Equivalently,

$$
\boxed{e_{BI}\le q+2m-2c_B.}
\tag{PN.9}
$$

Since every unpinned component has at least three boundary contacts,

$$
\boxed{3c_I+2c_B\le q+2m.}
\tag{PN.10}
$$

PN.10 by itself is not closing, but it makes the local meaning of the variables explicit: a missing unit hull side releases two loaded contact-degree slots, while every extra loaded chord consumes two.

---

## 4. Small primitive-defect classification

PN.6 says `m+k>=2`. Equality is rigid.

Assume

$$
m+k=2.
\tag{4.1}
$$

Then PN.4 forces

$$
\boxed{c_I=s_C=c_B=0.}
\tag{4.2}
$$

Hence there are no unpinned vertices in the positive contact core, no extra pinned-contact stress dimensions, and no loaded-loaded contact chords beyond the unit hull sides. The complete positive contact core is therefore a subgraph of the convex hull cycle with exactly `q-m` unit side edges.

C12 gives connectedness of the positive contact core. A subgraph of a `q`-cycle containing exactly `q-m` cycle edges can be connected only for `m<=1`. Therefore the only possibilities are:

### PN-E0: closed loaded shell

$$
\boxed{m=0,\qquad k=2.}
\tag{4.3}
$$

Then every force-hull side is a unit contact and

$$
C=C_q
$$

on the nonisolated core.

### PN-E1: one-gap loaded path

$$
\boxed{m=1,\qquad k=1.}
\tag{4.4}
$$

Then exactly one force-hull side is nonunit, every other hull side is a unit contact, and

$$
C=P_q
$$

on the nonisolated core.

The algebraic possibility `m=2,k=0` would leave only `q-2` hull-cycle edges and is disconnected, contradicting positive-support connectivity.

Thus:

### Corollary PN.1 — exact two-unit primitive endpoint

If `m+d_H+s_Z=2`, then the complete nonisolated contact core is either an all-loaded unit convex cycle or an all-loaded convex unit path with one nonunit closing side. No interior contact component, extra loaded chord, or pinned-contact stress redundancy remains.

This is a finite classification, not an asymptotic statement.

---

## 5. One unit above the endpoint

If

$$
m+k=3,
$$

then PN.4 gives

$$
\boxed{c_I+s_C+c_B=1.}
\tag{5.1}
$$

Exactly one of the following occurs:

1. one unpinned contact component and no extra pinned stress or loaded chord;
2. one extra pinned-contact stress dimension and no unpinned component or loaded chord;
3. one extra loaded-loaded chord and no unpinned component or pinned surplus.

This gives a complete discrete trichotomy at the first nontrivial primitive defect level. Any finite small-defect campaign can therefore work case-by-case without hidden currencies.

---

## 6. Relation to KC and LH

LH gives

$$
e_{BB}=Q+2k+u_B+c_B.
$$

PN.4 supplies

$$
c_B=m+k-2-c_I-s_C.
$$

Combining them yields the alternative exact form

$$
\boxed{
e_{BB}
=Q+u_B+m+3k-2-c_I-s_C.}
\tag{PN.11}
$$

This makes clear why the coarse currencies in KC are coupled: direct loaded-loaded contacts are not an independent resource once the primitive boundary topology is fixed.

The exact terminal count PN.3 and contact count PN.11 together imply

$$
\boxed{
e_{BB}-q
=k-2-c_I-s_C.}
\tag{PN.12}
$$

Of course PN.12 is also a rearrangement of ZU; the primitive normal form explains its geometry. In particular, `e_BB>q` is possible only if the mixed/diameter defect exceeds the combined interior-component and pinned-stress budget by more than two.

---

## 7. Metric boundary split retained

LH also gives

$$
x_B=(\operatorname{per}F-q)+(b-\operatorname{per}F).
$$

This does not turn `m` into a metric quantity with a uniform positive cost: a nonunit hull side can have length `1+o(1)`. PN therefore keeps `m` and `u_B` as separate integer currencies rather than replacing them by perimeter surplus.

This distinction is important for any stability proof near PN-E0/PN-E1.

---

## 8. Regression audit

### Regular odd shell

Here

$$
m=u_B=c_B=c_I=s_C=0,
\qquad k=s_Z=2.
$$

PN.4 gives `0=0`, and the configuration is exactly PN-E0.

### Unit square

Again

$$
m=u_B=c_B=c_I=s_C=0,
\qquad k=d_H=2,
$$

so the square is PN-E0, as required.

### One missing hull side with a unit boundary path

A convex unit path with one nonunit closing side has `m=1,c_B=c_I=s_C=0`. PN.4 forces `k=1` if it is to lie in the post-ZF exact ledger. PN-E1 records this possibility rather than falsely excluding it by topology alone.

### Two-edge outer detour

A nonunit hull side replaced by a two-edge unit path through an unpinned vertex has `m=1` but also `c_I>=1`; PN.4 correspondingly requires `m+k>=3`. The intermediate mechanical structure is therefore paid for explicitly.

---

## 9. What this changes

The post-ZF branch can now be organized by the primitive defect

$$
\boxed{p:=m+k=m+d_H+s_Z.}
$$

rather than by several partially overlapping surpluses.

- `p=2` is completely classified by PN-E0/PN-E1.
- `p=3` has exactly one interior/stress/chord defect.
- for general `p`, PN.4 says there are exactly `p-2` objects counted by `c_I+s_C+c_B`.

This is useful for both finite exclusion and stability: any argument that forces many interior components, extra pinned stresses, or loaded chords automatically forces the same amount of primitive boundary/mixed defect.

It does **not** yet give a lower bound `p=Omega(D)`. Large `u_B` or `Q` can make `q` large while `p` stays small, so such a claim would be false from the ledgers alone.

---

## 10. Next theorem

There are now two especially sharp endpoints.

1. **Small `p=m+k`.**  Exclude or classify PN-E0 and PN-E1 for sufficiently large global minimizers, then prove stability when `p=o(D)`. This is a boundary-shell/rattler problem with no hidden interior contact topology at the exact endpoint.
2. **Large `p`.** PN.4 automatically gives a large combined `c_I+s_C+c_B`, which can be fed into attachment-cell, response-rank, or loaded-chord geometry.

The immediate finite target is PN-E1: an all-loaded convex contact path whose only nonunit hull side closes the force polygon. Any exclusion of PN-E1 plus an existing exclusion of the pure cyclic shell endpoint would raise the primitive defect floor above two.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

The identities are exact but depend on the report-level LH/ZT/ZU/ZK stack.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Primitive variables:
  m   = number of nonunit loaded hull sides,
  u_B = x_B-m,
  c_B = e_BB-(q-m),
  k   = d_H+s_Z.

Exact normal form:
  x_B = m+u_B,
  q = m+u_B+Q+2k,
  e_BB = q-m+c_B,
  c_I+s_C+c_B = m+k-2,
  sum delta_r+R_I+s_B+k = 6+u_B+Q+2s_C+c_B,
  e_BI+2c_B+s_B = q+2m.

Hence m+k>=2.
If m+k=2, then c_I=s_C=c_B=0 and positive-contact connectivity leaves only:
  PN-E0: m=0,k=2, C=C_q (all-loaded unit convex cycle);
  PN-E1: m=1,k=1, C=P_q (one nonunit closing hull side).
If m+k=3, exactly one of c_I,s_C,c_B equals one.

Next: exclude PN-E1 or prove a stability theorem forcing p=m+k=Omega(D).
```
