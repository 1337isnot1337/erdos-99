> Generated reading edition · [exact source](../../../docs/reports/target_c_pinned_surplus_distinct_attachments_2026-09-10.md) · source SHA-256 `b10c391049b117d1dd782dd63ec35b8636c03c1829869f2cf8ad51cd85aa9666`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A259D18BDE39","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — pinned surplus is bounded by distinct attachment excess

**Date:** 2026-09-10  
**Repository state:** branch from `1ea7a3c5970d614c9f860841eea5ad3718ca171f`  
**Run type:** exact planar rigidity/incidence sharpening  
**Target:** Target C C-II after ZF/ZJ/ZK  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

For an unloaded component `I_r`, let

- `n_r=|I_r|`;
- `e_r` be its internal contact edges;
- `t_r` be its contact edges to loaded terminals;
- `A_r` be the set of distinct loaded attachment terminals;
- `a_r=|A_r|>=3`;
- `s_r=e_r+t_r-2n_r-1>=0` be its extra pinned-contact left nullity.

The existing ledgers treat `s_r` as a raw stress currency.  Planarity gives a sharper interpretation: every unit of pinned surplus requires a **new distinct loaded attachment**, not merely another attachment edge.

### Theorem PA.1 — component pinned-surplus bound

For every unloaded component,

$$
\boxed{s_r\le a_r-3.}
\tag{PA.1}
$$

Equivalently,

$$
\boxed{e_r+t_r\le2n_r+a_r-2.}
\tag{PA.2}
$$

Summing over components and using ZJ's

$$
u_A:=\sum_r a_r-3c_I,
$$

gives

$$
\boxed{s_C\le u_A.}
\tag{PA.3}
$$

Combining PA.3 with the exact ZJ identity yields a new universal defect bound

$$
\boxed{d_H+s_Z\le e_{BB}.}
\tag{PA.4}
$$

Thus pinned nullity cannot pay for diameter-tree defect or extra mixed-framework dependencies. Those defects require actual loaded-loaded unit contacts.

---

## 1. Strict harmonic containment

C36 proves

$$
I_r\subseteq\operatorname{conv}A_r.
$$

For the planar augmentation below it is useful to record the strict form.

### Lemma PA.0

Every vertex of `I_r` lies in the interior of

$$
P_r:=\operatorname{conv}A_r.
$$

### Proof

Suppose `x in I_r` lies on `partial P_r`. Choose a supporting linear functional `ell` of `P_r` with

$$
ell(x)=\max_{a\in A_r}\ell(a)=M.
$$

C36's harmonic maximum principle already gives `ell(y)<=M` for every component vertex. At `x`, positive contact equilibrium writes `x` as a strict weighted average of its contact neighbors. Equality at the maximum forces every contact neighbor of `x` to have `ell=M`.

Connectedness propagates this equality through all of `I_r`. At every component vertex incident to an attachment edge, the same weighted-average equality forces that loaded attachment to have `ell=M`. Hence every point of `A_r` lies on the supporting line `ell=M`.

But `a_r>=3`, and the points of `A_r` are distinct extreme vertices of the convex force hull. They cannot all be collinear. Contradiction. `square`

Therefore all original internal and attachment contact edges lie in `P_r`, and only their loaded endpoints can meet `partial P_r`.

---

## 2. Boundary-cycle augmentation

Form a plane graph `J_r` with vertex set

$$
V(J_r)=I_r\sqcup A_r
$$

and edge set consisting only of

1. the `e_r` internal contact edges of `I_r`, and
2. the `t_r` attachment contact edges from `I_r` to `A_r`.

Loaded-loaded contact edges are deliberately omitted.  The graph `J_r` is connected.

Because `A_r` is a subset of the extreme vertices of the convex polygon `F`, the points of `A_r` are themselves in strict convex position. Add the `a_r` sides of their convex cycle `partial P_r`. By Lemma PA.0 these added sides do not pass through component vertices, and by planarity of the contact graph they cross no edge of `J_r`.

Call the augmented plane graph `J_r^+`. It has

$$
V^+=n_r+a_r,
\qquad
E^+=e_r+t_r+a_r.
\tag{2.1}
$$

Its outer face is the simple `a_r`-cycle `partial P_r`.

---

## 3. Count triangular faces

The original contact graph is triangle-free. Therefore a triangular bounded face of `J_r^+` must use at least one newly added boundary-cycle edge.

It cannot use two boundary-cycle edges: two adjacent boundary edges have three loaded endpoints, and closing such a triangle would require an edge between two loaded vertices, while `J_r` contains no loaded-loaded edges. Three boundary-cycle edges can only be the outer triangle itself when `a_r=3`, not a bounded face of the graph containing `I_r`.

Hence every triangular bounded face uses **exactly one** added boundary edge. Each added boundary edge is incident to at most one bounded face, the other side being exterior to `P_r`. If `T_r` denotes the number of triangular bounded faces,

$$
\boxed{T_r\le a_r.}
\tag{3.1}
$$

Every other bounded face has boundary-walk length at least four.

Let `f_r` be the number of bounded faces of `J_r^+`. Euler gives

$$
f_r=E^+-V^++1.
\tag{3.2}
$$

The outer face has length `a_r`, so the sum of bounded-face walk lengths is

$$
2E^+-a_r.
\tag{3.3}
$$

Therefore

$$
2E^+-a_r
\ge
3T_r+4(f_r-T_r)
=4f_r-T_r.
\tag{3.4}
$$

Substitute (3.2):

$$
2E^+-a_r
\ge
4(E^+-V^++1)-T_r.
$$

Rearranging,

$$
E^+
\le
2V^+-2-\frac{a_r}{2}+\frac{T_r}{2}
\le
2V^+-2.
\tag{3.5}
$$

Using (2.1),

$$
e_r+t_r+a_r
\le
2(n_r+a_r)-2,
$$

so

$$
\boxed{e_r+t_r\le2n_r+a_r-2.}
$$

Subtract `2n_r+1`. This is PA.1:

$$
\boxed{s_r\le a_r-3.}
$$

`square`

---

## 4. Global pinned-surplus consequence

The pinned blocks are disjoint over unloaded components, so ZK gives

$$
s_C=\sum_rs_r.
$$

Sum PA.1:

$$
s_C
\le
\sum_r(a_r-3)
=\left(\sum_ra_r\right)-3c_I
=u_A.
$$

This proves PA.3.

The exact ZJ identity is

$$
e_{BB}+s_C-k
=u_A+p_A+2(s-1)+u_0,
\qquad
k=d_H+s_Z,
\tag{4.1}
$$

with all slacks on the right nonnegative. Rearrange:

$$
e_{BB}-k
=(u_A-s_C)+p_A+2(s-1)+u_0.
\tag{4.2}
$$

PA.3 makes every term on the right nonnegative. Hence

$$
\boxed{k=d_H+s_Z\le e_{BB}.}
$$

More precisely, PA.4 has the exact remainder decomposition

$$
\boxed{
e_{BB}-(d_H+s_Z)
=(u_A-s_C)+p_A+2(s-1)+u_0.
}
\tag{PA.5}
$$

This identifies every unit by which loaded-loaded contacts exceed mixed defect.

### Case `c_I=0`

ZJ is stated for `c_I>0`. If `c_I=0`, then `s_C=0`, and ZU reads

$$
e_{BB}=q-2+k.
$$

Since a nondegenerate large force hull has `q>=2`, this also gives `k<=e_{BB}`. Thus PA.4 is universal across the post-ZF branch.

---

## 5. Equality structure

PA.1 is sharp. A singleton component at the center of four loaded pins on a unit circle has `n_r=1`, `e_r=0`, `t_r=a_r=4`, and `s_r=1=a_r-3`; no unit triangle is forced if consecutive pin distances exceed one.

The proof records the exact equality conditions. If

$$
s_r=a_r-3,
$$

then equality must hold throughout (3.4)--(3.5). Therefore

1. `T_r=a_r`: every added side of `P_r` bounds one triangular augmented face;
2. every other bounded face of `J_r^+` has degree exactly four.

Since every non-boundary edge in `J_r^+` is a unit contact edge, each nontriangular quadrilateral face is a unit-edge quadrilateral and hence a rhombus. Every triangular boundary face has two unit contact sides and one added attachment-hull side. Triangle-freeness forces that added side to have length strictly greater than one.

Thus equality in PA.1 has a concrete geometric normal form: a unit-rhombic disk capped along every attachment-hull side by an isosceles two-unit-side triangle.

---

## 6. Exact zero-loaded-contact branch

Suppose

$$
e_{BB}=0.
\tag{6.1}
$$

PA.4 forces

$$
\boxed{d_H=s_Z=0.}
\tag{6.2}
$$

If `c_I>0`, ZJ.4--ZJ.5 and PA.3 then force equality in every remaining incidence slack:

$$
\boxed{
u_A=s_C,
\qquad
p_A=0,
\qquad
s=1,
\qquad
u_0=0.
}
\tag{6.3}
$$

Indeed (4.2) has zero left side, so all nonnegative terms vanish.

Consequences:

- every loaded terminal is used by at least one unloaded component;
- the attachment-incidence graph is connected;
- C37's planar incidence bound is exact;
- the sum of PA.1 is exact, so every component individually satisfies `s_r=a_r-3` and has the rhombic equality form of Section 5.

The PC/TN exact outer-boundary ledger sharpens this further. With `e_BB=k=0`,

$$
e_{BB}=d_P+Q+2k+c_B
$$

forces

$$
\boxed{d_P=Q=c_B=0.}
\tag{6.4}
$$

and

$$
q=a_{miss}+d_P+Q+2k
$$

forces

$$
\boxed{a_{miss}=q.}
\tag{6.5}
$$

Here `a_miss` is the PC number of missing force-hull contact sides, not the incidence count `sum a_r`. Hence every force-hull side is noncontact, every OP outer pocket is triangular, and every bounded contact face has degree four. Since all its edges are unit contacts, every bounded contact face is a unit rhombus.

Finally `d_H=q-h=0`, so `h=q`. The planar diameter graph on its `q` nonisolated terminals is in the unicyclic odd-cycle case of the canonical diameter-graph classification: no tree component can remain when `q-h=0`. Thus the zero-loaded-contact survivor has the exact global form

```text
one odd diameter cycle on all loaded terminals
+ no loaded-loaded unit contacts
+ triangular two-contact outer pockets along every force-hull side
+ a contact core whose bounded faces are unit rhombi
+ each unloaded component saturating the pinned/attachment planar bound.
```

This is a strict structural reduction of the high-pinned-surplus branch. It does not yet prove that this rhombic-disk/odd-cycle form is impossible.

---

## 7. Asymptotic low-loaded-contact consequence

PA.4 also gives immediately

$$
e_{BB}=o(D)
\quad\Longrightarrow\quad
 d_H=o(D),\ s_Z=o(D).
\tag{7.1}
$$

Thus any high-`s_C`, low-`e_BB` survivor has an asymptotically unicyclic diameter graph and asymptotically minimal mixed-framework surplus. The pinned currency cannot conceal linear diameter-tree defect.

This is the correct branch to attack if the new FSJC/FN lower bound is carried mostly by `s_C` rather than by loaded-loaded contacts.

---

## 8. Regression audit

| Regression | Result |
| --- | --- |
| singleton tripod cell (`a_r=3,s_r=0`) | equality in PA.1 |
| singleton four-pin cell (`a_r=4,s_r=1`) | equality; shows PA.1 cannot be lowered universally |
| singleton five-pin cell (`a_r=5,s_r=2`) | equality is combinatorially allowed and geometrically compatible with pairwise distances `>1` on a unit circle |
| one component attached to all terminals | allowed; PA.1 scales with the number of distinct pins |
| multiple contacts from one loaded pin to one component | handled: `t_r` counts all such edges while `a_r` counts the pin once; the planar face proof still bounds the surplus |
| nested/noncrossing attachment cells | handled componentwise; no disjoint-cell assumption is used |
| regular odd shell | `c_I=s_C=0`; PA.3 is vacuous and PA.4 reduces to `d_H+s_Z<=e_BB`, which the shell can satisfy |
| dense isolated filling | untouched; isolates are outside the pinned blocks and remain the source-capacity obstruction |

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| strict `I_r subset int conv(A_r)` | proved | harmonic maximum principle plus three noncollinear extreme attachments |
| `s_r<=a_r-3` | proved | boundary-cycle augmentation and exact planar face count |
| `s_C<=u_A` | proved | sum over pinned blocks |
| `d_H+s_Z<=e_BB` | proved | exact ZJ remainder plus PA.3; ZU handles `c_I=0` |
| component equality normal form | proved combinatorially/geometrically | equality forces all boundary augmented faces triangular and all others unit rhombi |
| exact `e_BB=0` global normal form | proved from PA + ZJ + PC/TN + diameter-graph classification |
| exclusion of that normal form | open | requires new force/area/rearrangement input |
| Level I | open | high loaded-contact branch and rhombic odd-cycle branch remain |

---

## 10. Promotion recommendation

**Hold as report pending independent audit.** PA.1--PA.5 are exact and use only C36, pinned rank-nullity, planarity, and the audited ZJ ledger. If accepted, PA.4 should replace the weaker ZJ.7 estimate

$$
d_H+s_Z\le s_C+e_{BB}
$$

in the live post-ZF frontier.

---

## 11. Remaining closing implication

The new split is sharper:

1. `e_BB` linear: exploit many unit contacts among convex loaded diameter terminals;
2. `e_BB=o(D)`: PA forces `d_H+s_Z=o(D)`, so the diameter graph is asymptotically unicyclic and the mixed framework is near the `s_Z=0` circuit regime while FSJC/FN forces the linear currency into `s_C`.

The exact `e_BB=0` endpoint is now a rhombic disk with triangular outer pockets and one odd diameter cycle. A closing theorem should exclude that geometry by the actual KKT force balance or produce a strict sub-`D` competitor. Merely increasing the scalar lower bound on `e_BB+2s_C` is not the next target.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New PA theorem:
For every unloaded component I_r with a_r distinct loaded attachments,
    s_r=e_r+t_r-2n_r-1 <= a_r-3.
Hence, with u_A=sum a_r-3c_I,
    s_C<=u_A.
ZJ therefore sharpens exactly to
    e_BB-(d_H+s_Z)
      =(u_A-s_C)+p_A+2(s-1)+u_0 >=0,
so universally
    d_H+s_Z<=e_BB.

If e_BB=0, then d_H=s_Z=0 and all incidence slacks vanish:
    u_A=s_C, p_A=0, s=1, u_0=0.
PC/TN then gives d_P=Q=c_B=0 and every force-hull side is missing as
a contact. Thus every outer pocket is triangular, every bounded contact face is
a unit rhombus, every unloaded component saturates the PA bound, and H is the
single odd-cycle diameter case.

Remaining target: exclude this rhombic-disk/odd-cycle geometry or the complementary
linear loaded-loaded-contact branch.
```