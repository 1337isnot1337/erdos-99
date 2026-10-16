<!-- theorem-state: {"artifact_id":"ART-6E626A5A4BA2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHP: hinge rank forces diameter-path peeling along every long bridge segment

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-bridge-hinge-interval`  
**Run type:** exact local-rank consequence of ZHI/ZHAI  
**Target:** Target C physical-bridge branch  
**Depends on:** ZHI, ZHAI, ZF  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZHI gives one independent contact-preserving hinge coordinate per physical contact bridge and forces the active diameter rows to have rank at least `L-1` on any `L` consecutive hinges. ZHAI shows that all diameter rows sharing one topological separating interval span at most three dimensions.

Apply those facts to an arbitrary consecutive `L`-bridge segment. Every diameter edge whose block-tree route traverses the entire segment belongs, after restriction to those `L` columns, to the same full-interval affine class and therefore contributes total rank at most three. Every remaining diameter row contributes rank at most one.

Hence at least

\[
\boxed{L-4}
\]

active diameter rows must enter, leave, or terminate inside every `L`-bridge segment.

Taking `L=H` for a complete macroscopic trunk gives the stronger global support statement

\[
\boxed{m_{\rm peel}\ge H-4,}
\]

where `m_peel` counts distinct active diameter rows whose trunk interval is nonempty but does not cover the whole trunk.

This is a local theorem for arbitrary subtrunks such as the ZHT macroscopic trunk. It is distinct from the older common-route theorem. Canonical C24 combined with C26 is already stronger on the universal intersection: in fully force-visible C-II, the common intersection of all active diameter paths is either one bridge block or one universal contact bridge and never contains two bridge edges.

---

## 1. Localize the hinge construction to a subtrunk

Take any consecutive physical bridge segment

\[
J=\{f_{s+1},f_{s+2},\ldots,f_{s+L}\}
\tag{1.1}
\]

inside a contact bridge-tree path. Root the tree on the side before `f_{s+1}` and define the `L` descendant hinge rotations exactly as in ZHI.

The ZHI proof is local to a consecutive bridge chain. Therefore these `L` hinge fields are linearly independent, preserve every contact length to first order, and their intersection with the Euclidean infinitesimal motions has dimension at most one.

Let

\[
G_J
\tag{1.2}
\]

be the active diameter first-derivative matrix restricted to these `L` hinge coordinates.

ZF mixed infinitesimal rigidity gives

\[
\boxed{\operatorname{rank}G_J\ge L-1.}
\tag{ZHP1}
\]

If the root shore of the first bridge in the segment contains at least two vertices, the stronger anchored form gives

\[
\boxed{\operatorname{rank}G_J=L.}
\tag{ZHP2}
\]

---

## 2. Full traversers form one rank-three affine class

Call an active diameter edge `h=xy` a **full traverser of J** if its bridge-tree path contains every bridge of `J`.

For such a row, the same endpoint remains on the descendant side throughout all `L` cuts. ZHAI's exact coefficient formula on the segment is

\[
G_{h,j}=c_h-2d_h\cdot Jp_{a_j},
\qquad j\in J,
\tag{2.1}
\]

with `d_h=p_x-p_y` and one row-dependent scalar `c_h`.

Hence, after restriction to `J`, all full-traverser rows lie in the common three-dimensional space

\[
\operatorname{span}
\left\{
(1)_{j\in J},
(a_{j,x})_{j\in J},
(a_{j,y})_{j\in J}
\right\}.
\tag{2.2}
\]

Therefore

\[
\boxed{\operatorname{rank}G_J^{\rm full}\le3.}
\tag{ZHP3}
\]

This includes arbitrarily many full-traversing diameter edges. Their count can be large, but their first-order action on the bridge hinges has only three degrees of freedom.

---

## 3. Every long segment needs linearly many peeling rows

Let `P_J` be the set of active diameter rows that

1. have nonzero hinge action on at least one column of `J`; and
2. are not full traversers of `J`.

Put

\[
m_J:=|P_J|.
\tag{3.1}
\]

Zero rows do not affect rank. Every row in `P_J` increases row rank by at most one, while all full traversers together contribute rank at most three. Thus

\[
\operatorname{rank}G_J\le3+m_J.
\tag{3.2}
\]

Combining with ZHP1 proves:

### Theorem ZHP.1 — local diameter-path peeling

For every consecutive `L`-bridge segment,

\[
\boxed{m_J\ge L-4.}
\tag{ZHP4}

In the anchored rank-`L` case,

\[
\boxed{m_J\ge L-3.}
\tag{ZHP5}

Every counted row has a topological trunk interval that overlaps `J` but does not cover it. Consequently at least one endpoint of that interval lies inside the closed segment `J`: the corresponding diameter path enters or leaves the trunk within the segment.

No KKT-weight lower bound is used. ZHP is a hard support/routing statement.

---

## 4. Reconciliation with C24/C26

C23 gives a common bridge-block-tree hub for all active diameter paths. C24 identifies their complete intersection and shows that any internal common-route blocks collapse to a straight reaction-free chain.

Canonical C26 later eliminates unloaded degree-one/two contact vertices and reaction-free two-terminal regions in fully force-visible C-II. Therefore the active canonical stack already implies:

\[
\boxed{
\text{the common intersection is either one bridge block or one universal physical bridge.}
}
\tag{4.1}

So ZHP is not used to improve the universal common-route length. Its role begins strictly beyond the common intersection, on long branch/trunk segments through nontrivial bridge blocks where different diameter paths peel at different depths.

---

## 5. Complete-trunk consequence

Apply ZHP directly to the complete ZHT trunk of length `H`. Let

\[
P_{\rm peel}
\]

be the set of active diameter rows that act nontrivially on the trunk but do not traverse all `H` trunk bridges. ZHP4 with `L=H` gives immediately

\[
\boxed{|P_{\rm peel}|\ge H-4.}
\tag{ZHP6}

In the anchored case,

\[
\boxed{|P_{\rm peel}|\ge H-3.}
\tag{ZHP7}

Thus essentially one distinct non-full-traversing diameter row is required per physical bridge hinge. Every such row has at least one trunk-interval endpoint in the corridor.

For the PR #111 ZHT trunk,

\[
H\ge\frac{\eta^2}{16\pi}D,
\]

so

\[
\boxed{|P_{\rm peel}|\ge\frac{\eta^2}{16\pi}D-O(1).}
\tag{ZHP8}

This is stronger than the first fixed-window `H/4-O(1)` corollary and requires no secondary double counting.

The theorem does not say the peel locations themselves are all distinct. ZHAI separately controls repeated interval classes: one fixed interval class has row rank at most three, so exact mixed rigidity also forces linearly many distinct routing intervals.

---

## 6. Relation to ZHA and ZHAI

ZHA already assigns a distinct loaded attachment to every internal route block of the captured harmonic cell. ZHP is not another attachment-count theorem. It says the **active diameter constraints themselves** must peel along the trunk at linear support density.

ZHAI gives

\[
H-1\le2N_{star}+m_{ns}.
\]

ZHP adds a routing restriction: even a large star or nonstar support cannot obtain the necessary hinge rank if nearly all of its rows traverse the same full trunk. At least `H-4` distinct active rows must have a proper trunk interval.

Thus the surviving ZHT branch simultaneously has

1. `Omega(D)` independent physical hinge coordinates;
2. `Omega(D)` distinct loaded attachments from ZHA;
3. `Omega(D)` distinct proper-interval active diameter rows from ZHP;
4. linearly many distinct topological interval classes from ZHAI;
5. only one possible universal physical bridge by canonical C24/C26.

In the C66 near-zero phase, the additional proper-interval diameter rows may still carry arbitrarily small total beta mass.

---

## 7. Why this is not yet a contradiction

A caterpillar-like diameter support can realize linear peeling: one long star family may carry most of the beta mass while many low-weight diameter edges terminate in side branches along successive trunk blocks and provide exact hinge rank. This is compatible with the support-versus-weight regression.

Therefore ZHP does not infer a beta-mass floor from peeling count.

The next geometric target is:

> **peeling-capacity theorem.** Bound the active proper-interval diameter rows that can coexist with a `D+o(D)` near-geodesic ZSP corridor, convex diameter-thrackle geometry, and the ZCQ separation between central route vertices and loaded diameter endpoints.

A successful sublinear capacity bound would exclude the low-reset bridge branch without needing a transverse-stress floor.

---

## 8. Regression audit

### Canonical universal route

Already controlled more strongly by C24+C26: at most one universal physical bridge. ZHP is not counted as progress on this subcase.

### Long trunk with one tiny-beta diameter row peeling at each block

Compatible. This is now the sharp support-level regression.

### Repeated peel location with many distinct rows

Allowed; ZHP counts rows, not distinct locations. ZHAI's interval-class rank bound is the complementary restriction.

### Exceptional rhombic faces

Irrelevant. The theorem is purely bridge-tree kinematics plus mixed rigidity and incurs no exceptional-face loss.

---

## 9. Classification

**Status:** proved report-level local consequence of ZHI/ZHAI and ZF; reconciled with the stronger canonical C24/C26 universal-route theorem.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHP:
For any L consecutive physical contact bridges, ZHI gives L independent descendant
hinges and ZF gives active-diameter rank >=L-1 on them. All diameter rows traversing
the complete segment have
    G_hj=c_h-2 d_h dot J a_j,
so the full-traverser family has rank <=3. Therefore at least L-4 distinct active
diameter rows act on the segment without traversing it fully (L-3 anchored).

Apply this to the complete ZHT trunk:
    |P_peel| >= H-4 >= eta^2 D/(16pi)-O(1).
These are actual proper-interval diameter constraints, not merely loaded attachments.
ZHA separately gives one distinct attachment per route block; ZHAI says each fixed
interval class has rank <=3.

C24+C26 already give the stronger canonical universal-route fact (at most one physical
bridge), so no weaker common-route claim is made.

Remaining regression:
one high-beta long star family plus nearly one tiny-beta proper-interval diameter row
per trunk hinge. Next target is to exclude that caterpillar-like peeling support using
ZSP near-geodesic geometry and the convex diameter-thrackle constraints.
```
