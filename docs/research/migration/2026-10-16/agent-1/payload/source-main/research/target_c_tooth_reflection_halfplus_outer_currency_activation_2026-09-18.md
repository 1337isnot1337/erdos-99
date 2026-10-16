# Target C-II — half-plus FREE matching pays outer-pocket currency and admits vanishing contact activation

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only bridge from the fixed-pair directional-defect theorem  
**Scope:** `PAIR-REUSE` for the two extreme all-inactive FREE modules  
**Dependencies:** two-normal lower directional defect; two-sided outer-face localization; OP outer-pocket Oler absorption; short inactive-edge planarity  
**Certificate:** `research/verify_target_c_tooth_reflection_halfplus_outer_currency_activation_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The fixed-pair directional-defect theorem forces slightly more than `D/2` disjoint inverse-`D` near-unit pairs in the original outer contact face. This note spends that conclusion in two ways that were not recorded in the directional-defect note.

First, the **endpoints**, not only the edges, force a linear amount of already canonical outer-pocket/external-population currency. Second, a linear subfamily can be moved by only `O(1/D)` per point to create persistent new unit contacts while keeping the original diameter core, force hull, old contacts, and diameter exactly fixed.

Neither statement closes C-II. They replace the bare phrase “half-plus matching” by two source-level consequences that can be composed with the existing OP/ER/RA and outer-detour machinery.

Put

\[
h_*:=\frac{\sqrt{303}}{52},
\qquad
c_*:=0.129220199818177\ldots,
\qquad
\delta_*:=2\left(1-\cos\frac{c_*}{2}\right)
=0.00417301303247308\ldots .
\tag{HC.1}
\]

For fixed constants `K,J>h_*`, write

\[
\alpha_K:=1-\frac{h_*}{K},
\qquad
\mu_{K,J}:=
1+\frac{\delta_*\alpha_K}{4}-\frac{h_*}{J}.
\tag{HC.2}
\]

The directional-defect theorem gives a vertex-disjoint matching `M` of old fully inactive outer-face source pairs with

\[
\boxed{
|M|\ge\left(\frac{\mu_{K,J}}2-o(1)\right)D
}
\tag{HC.3}
\]

and

\[
\boxed{1<|x-y|\le1+\frac JD\qquad(xy\in M).}
\tag{HC.4}
\]

For `K=J=400`,

\[
\mu_{400,400}=1.000205510229962\ldots,
\qquad
\frac{\mu_{400,400}}2=0.500102755114981\ldots .
\tag{HC.5}
\]

The asymptotic fixed-cutoff envelope is

\[
\boxed{
\mu_\infty:=1+\frac{\delta_*}{4}
=1.001043253258118\ldots .
}
\tag{HC.6}
\]

## 1. The half-plus endpoints pay OP currency directly

Let

- `F` be the canonical force hull;
- `H_out` be the total OP outer-pocket area inside `F`;
- `b` be the unit-contact outer-face boundary-walk length;
- `P_F=per(F)`;
- `U_det:=b-P_F>=0` be the exact OP/OD outer chain-chord detour;
- `Z_ext` be the number of contact-isolated source points outside `F`;
- `Z_in` be the number of contact-isolated source points in `F` and in the outer contact face.

Every endpoint of `M` is an old fully inactive outer-face source point. The `2|M|` distinct endpoints therefore split between the populations counted by `Z_in` and `Z_ext`:

\[
2|M|\le Z_{in}+Z_{ext}.
\tag{HC.7}
\]

The exact OP theorem gives

\[
Z_{in}
\le
\frac{2}{\sqrt3}H_{out}
+\frac{P_F-b}{2}
=
\frac{2}{\sqrt3}H_{out}-\frac{U_{det}}2.
\tag{HC.8}
\]

Combining HC.3, HC.7, and HC.8 yields the finite-asymptotic currency inequality

\[
\boxed{
Z_{ext}
+\frac{2}{\sqrt3}H_{out}
-\frac{U_{det}}2
\ge
(\mu_{K,J}-o(1))D.
}
\tag{HC.9}
\]

Equivalently,

\[
\boxed{
Z_{ext}
+\frac{2}{\sqrt3}H_{out}
\ge
(\mu_{K,J}-o(1))D
+\frac{b-P_F}{2}.
}
\tag{HC.10}
\]

This is stronger than merely observing that the outer face contains `Theta(D)` isolated points. The same half-plus population is charged to the exact OP currency, and positive outer-walk detour makes the required payment larger rather than smaller.

Two immediate forms are useful.

If

\[
Z_{ext}\le (z+o(1))D,
\qquad z<\mu_{K,J},
\]

then

\[
\boxed{
H_{out}
\ge
\frac{\sqrt3}{2}(\mu_{K,J}-z)D
+\frac{\sqrt3}{4}(b-P_F)
-o(D).
}
\tag{HC.11}
\]

If instead

\[
H_{out}\le (h+o(1))D,
\]

then

\[
\boxed{
Z_{ext}
\ge
\left(\mu_{K,J}-\frac{2h}{\sqrt3}-o(1)\right)D
+\frac{b-P_F}{2}.
}
\tag{HC.12}
\]

In particular, under `Z_ext=o(D)`, letting the fixed cutoffs tend to infinity after the asymptotic argument gives

\[
\boxed{
H_{out}
\ge
(0.866928887608550\ldots-o(1))D
+\frac{\sqrt3}{4}(b-P_F).
}
\tag{HC.13}
\]

Conversely, if `H_out=o(D)`, then

\[
\boxed{
Z_{ext}
\ge
(1.001043253258118\ldots-o(1))D
+\frac{b-P_F}{2}.
}
\tag{HC.14}
\]

Thus a hard `PAIR-REUSE` survivor cannot have both sublinear external population and sublinear outer-pocket area.

## 2. A linear submatching can be activated by `O(1/D)` motions

The half-plus matching also gives a controlled representative transfer.

Choose one endpoint from every edge of `M`; call the chosen set `S`. Thus

\[
|S|=|M|.
\tag{HC.15}
\]

On `S`, form the auxiliary graph `Q_J` by joining `u,v` whenever

\[
|u-v|\le1+\frac JD.
\tag{HC.16}
\]

Every vertex of `S` was fully contact-inactive in the original source, so every edge of `Q_J` has length strictly larger than one. For fixed `J` and sufficiently large `D`,

\[
1+\frac JD<\sqrt2.
\]

The short-inactive-edge planarity theorem therefore makes `Q_J` a plane graph. Every finite plane graph is 5-degenerate, hence 6-colorable by the elementary greedy deletion argument. One color class is an independent set `T` with

\[
\boxed{|T|\ge\frac{|M|}{6}.}
\tag{HC.17}
\]

Consequently

\[
\boxed{
|T|
\ge
\left(
\frac1{12}
+\frac{\delta_*\alpha_K}{48}
-\frac{h_*}{12J}
-o(1)
\right)D.
}
\tag{HC.18}
\]

For `K=J=400`,

\[
\boxed{|T|\ge(0.0833504591858302\ldots-o(1))D.}
\tag{HC.19}
\]

The fixed-cutoff envelope is

\[
\boxed{
|T|\ge(0.0834202711048432\ldots-o(1))D.
}
\tag{HC.20}
\]

We now activate the vertices of `T` sequentially.

For each `v in T`, let `p(v)` be its partner in the original matching `M`. Only `v`, not `p(v)`, is designated as a mover. At the moment `v` is processed, move it along the straight segment toward `p(v)` and stop at the first unit-distance event with any current source point.

### Lemma HC.1 — every designated mover is still contact-inactive when its turn begins

Suppose an earlier mover `u in T` had first created a contact with a future mover `v in T`. The displacement of `u` before first contact is at most

\[
|u-p(u)|-1\le\frac JD.
\]

Therefore the original positions would satisfy

\[
|u-v|\le1+\frac JD,
\]

so `uv` would be an edge of `Q_J`, contradicting independence of `T`.

Thus no earlier first-hit contact uses a future mover. Every future mover remains contact-inactive until its own turn.

### Lemma HC.2 — every move exists, is at most `J/D`, and preserves diameter `D`

At the start of the move, all distances from `v` are strictly larger than one. Its partner `p(v)` is never moved, and

\[
1<|v-p(v)|\le1+\frac JD.
\]

If no other point becomes tight first, moving toward `p(v)` by exactly `|v-p(v)|-1` reaches unit distance from the partner. Hence a first unit event occurs after displacement at most `J/D`, and stopping at the first event preserves all lower metric inequalities.

Every moved point stays on a segment joining two original source points, hence remains in the original convex hull `K=conv(A)`. Since `diam(K)=D`, no upper metric inequality can be violated during any move.

All designated movers were diameter-inactive in the original source. Therefore every original actual-diameter endpoint remains fixed. At least one original diameter pair remains at distance exactly `D`, while all current distances are at most `D`. The diameter is therefore exactly `D` throughout.

### Lemma HC.3 — all created contacts persist

Original contacts never use a designated mover, because every mover was fully contact-inactive. Hence every old contact has fixed endpoints and survives.

By Lemma HC.1, the first contact created by a mover is never with a future mover. It is therefore incident only to points that will remain fixed afterwards (possibly a previously processed mover). That new contact persists through all later steps.

Different movers create distinct new contact edges because each such edge contains its own mover. Thus the terminal source has at least `|T|` more unit contacts than the original source.

Combining the lemmas gives:

### Theorem HC-ACT — vanishing-displacement contact-rich representative

From the `PAIR-REUSE` half-plus matching one can construct another source with the same cardinality and the same diameter `D` such that

1. every original source point moves by at most `J/D`;
2. all original actual-diameter endpoints remain fixed;
3. every original contact remains a contact;
4. the original force hull and original positive-force core remain geometrically fixed;
5. at least the number of contacts in HC.18 are newly created and persist.

Since the original source was a global minimum-diameter source for its cardinality, the terminal source is another global minimum-diameter representative. Any old equilibrium/force certificate supported only on the unchanged original core remains algebraically valid; the new contacts may be assigned zero multiplier.

This is a more local representative transfer than the existing full rattler-activation construction: on the linear family extracted here the maximum displacement is `O(1/D)`, not merely bounded by the container geometry.

## 3. What is now reduced, and what is not

The directional-defect theorem left a half-plus inactive matching with no source-wide expenditure attached to it. HC.9 supplies that expenditure exactly:

\[
\boxed{
\text{half-plus reuse}
\Longrightarrow
Z_{ext}+\frac{2}{\sqrt3}H_{out}-\frac12(b-P_F)
\ge(1.001043253\ldots-o(1))D
}
\]

in the fixed-cutoff envelope.

At the same time HC-ACT shows that a linear subset of those isolates can be made contact-active by vanishing pointwise displacement without changing the original diameter carrier or force hull.

This still does not prove C-II. Linear outer-pocket area and linear external population are both compatible with the currently promoted global bounds, and adding contacts produces a contact-richer global minimizer rather than contradicting the contact-minimal normalization of the original representative.

The remaining useful target is narrower: combine HC.9 with a branch in which the canonical outer-pocket/external currency is already `o(D)`, or prove that HC-ACT transfers enough of the reflection/outer-walk structure to the contact-richer representative to spend the newly created linear contact population. A proof must use one of those currencies; optimizing the `0.5005...` matching coefficient further is not the main obstruction.

**Disposition:** converted the fixed-pair half-plus matching into an exact OP external/pocket currency inequality and a vanishing-displacement same-diameter contact activation of a linear subfamily. C-II remains open.
