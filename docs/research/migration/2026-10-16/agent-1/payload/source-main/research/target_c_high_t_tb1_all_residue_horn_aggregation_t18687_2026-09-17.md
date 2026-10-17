# Target C-II — all six exact-swap residue classes aggregate to a two-way Horn obstruction

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the one-sign strong-TB1 Horn branch; no canonical promotion claimed  
**Scope:** one-sign strong-TB1 exact swaps through `t=(q-k)/D<=1.8687`  
**Dependencies:** five-row capsule theorem; six-spaced Horn reduction; Horn poison-forest theorem; source-pair layer-support multiplicity; Oler O--O path-capacity theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_all_residue_horn_aggregation_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The six-spaced Horn theorem keeps one largest residue class modulo six and obtains a three-way alternative: permanent LOWER blockers, permanent UPPER blockers, or an UPPER implication forest. The factor-six thinning is needed only inside one simultaneous exact-swap system. It is not necessary to discard the other five residue classes globally.

Run the Horn reduction separately on all six residue classes. The six systems are never swapped simultaneously with one another; canonical minimality is applied independently to each valid six-spaced subsystem. Then aggregate the geometric blockers returned by the six poison-forest theorems.

The key exact multiplicity fact is source-wide:

\[
\boxed{
\text{one source pair can be affected by swaps at at most two physical path layers.}
}
\tag{AR.1}
\]

Thus a blocker pair extracted from several residue-class Horn systems is counted at most twice in their union.

This removes the implication-forest branch at the global level and gives a clean two-way alternative.

> **All-residue Horn aggregation theorem.** Let
> \[
> s_0={791\over320{,}000{,}000}.
> \]
> In the one-sign strong-TB1 branch, for all sufficiently large `D`, one of the following holds:
>
> **GLOBAL LOWER:** there are more than
> \[
> \boxed{
> \left({s_0\over48}-o(1)\right)D
> =
> (5.14973958333\ldots\times10^{-8}-o(1))D
> }
> \tag{AR.2}
> \]
> distinct permanent inverse-`D` near-unit blockers, each with exact O--O path bandwidth at most five;
>
> or
>
> **GLOBAL UPPER:** there are more than
> \[
> \boxed{
> \left({s_0\over48}-o(1)\right)D
> }
> \tag{AR.3}
> \]
> distinct inverse-`D` near-diameter UPPER blockers with an injective retained-coordinate ownership map and exact selected-cut interval support.
>
> The UPPER family may contain both permanent upper blockers and implication-forest pairs; that distinction is no longer needed downstream.

The common coefficient is

\[
\boxed{
\beta_*:={s_0\over48}
={791\over15{,}360{,}000{,}000}
=5.14973958333\ldots\times10^{-8}.
}
\tag{AR.4}
\]

For UPPER localization this doubles the currently available six-spaced owned-upper input `gamma_6/8=s_0/96`. Combining (AR.3) with the path-specific Oler cap

\[
A_*={14\over3\sqrt3}
\]

upgrades the flexible-scale same-type coefficient to

\[
\boxed{
c_{\rm all}
:={\beta_*\over6A_*}
={791\sqrt3\over430{,}080{,}000{,}000}
=3.18557521574\ldots\times10^{-9}.
}
\tag{AR.5}

Hence for every scale `L_D->infinity` with `L_D=o(D)`, GLOBAL UPPER yields either

\[
(c_{\rm all}-o(1))L_D
\]

SIGNED or THIN blockers on one common low-defect selected row, or that many same-type blockers inside one `2L_D+O(1)` low-defect path window. The dense common train scaffold and circumcenter-flank conclusions are unchanged.

---

## 1. Partition the entire one-sign population, not just one largest class

Let `M_D` be the one-sign strong-TB1 coordinate set. On this branch the existing contact-swap split gives

\[
|M_D|>
\left({s_0\over2}-o(1)\right)D.
\tag{AR.6}
\]

The genuine-upper binary theorem identifies only `O(1)` exceptional source pairs. Delete every coordinate incident to one of those pairs before partitioning. Since a source pair has only two endpoints, this removes only `O(1)` coordinates source-wide.

Call the remaining coordinate set `P_D`, so

\[
\boxed{
|P_D|>
\left({s_0\over2}-o(1)\right)D.
}
\tag{AR.7}
\]

Partition by path index modulo six:

\[
P_D=P_0\sqcup\cdots\sqcup P_5.
\tag{AR.8}
\]

Every `P_r` is six-spaced. The five-row capsule theorem says every LOWER singleton blocker has endpoint-region distance at most five. Therefore, inside each `P_r`, a LOWER blocker depends on only one retained Boolean coordinate. The simultaneous active-contact/old-diameter decoupling and Horn reduction apply exactly as in the six-spaced theorem.

No assertion is made that swaps from different residue classes can be combined. We use six separate valid finite-swap systems on the same source.

---

## 2. Per-class poison output can be reduced to LOWER versus UPPER

Fix a residue class `P_r` of size

\[
p_r:=|P_r|.
\]

Apply the Horn poison-forest theorem to its implication digraph and forbidden set.

If the forbidden set has size at least `p_r/2`, then one metric type supplies at least half of the chosen forbidden-coordinate incidences.

- If LOWER wins, six-spacing plus five-row bandwidth makes every chosen lower pair unique to its coordinate inside `P_r`. Thus the class supplies at least
  \[
  {p_r\over4}-O(1)
  \]
  distinct LOWER blockers.

- If UPPER wins, one upper source pair can poison at most two retained coordinates. Thus the class supplies at least
  \[
  {p_r\over8}-O(1)
  \]
  distinct UPPER blockers.

If the forbidden set has size below `p_r/2`, shortest paths to the forbidden set give more than

\[
{p_r\over2}
\]

distinct implication-forest arcs. Every arc is an UPPER near-diameter source pair. This is stronger than the `p_r/8` UPPER floor needed below.

Therefore every residue class may be assigned one of two labels:

\[
\boxed{
\begin{array}{ll}
L:& \ge p_r/4-O(1)\text{ distinct LOWER blockers},\\[1ex]
U:& \ge p_r/8-O(1)\text{ distinct UPPER blockers}.
\end{array}
}
\tag{AR.9}
\]

The `U` label absorbs both permanent-upper and implication-forest outcomes.

---

## 3. Cross-residue blocker multiplicity is at most two

Let `xy` be any previously strict source pair. A physical-layer translation changes `xy` exactly when one endpoint lies in the translated layer and the other does not.

Every source vertex lies in at most one physical path layer. Therefore `xy` can be affected only at the layer containing `x` and the layer containing `y`:

\[
\boxed{
\#\{i:\text{the swap at layer }i\text{ changes }xy\}\le2.
}
\tag{AR.10}
\]

This is independent of residue class and independent of whether the pair is LOWER, permanent UPPER, or an implication pair.

Consequently, if the six classwise extractions contain `Q` blocker occurrences in total, their union contains at least `Q/2` distinct source pairs.

The ownership tags can also be retained injectively after deduplication. Within a permanent-blocker extraction, one blocker occurrence was chosen for each coordinate, so different blocker pairs may be assigned different chosen coordinates. Within an implication forest, every selected arc has a distinct tail. Across residue classes the coordinate sets are disjoint. If a source pair appears twice, retain one occurrence and its owner. Thus every distinct retained UPPER blocker can be assigned a different retained coordinate lying at one of its endpoints.

---

## 4. Balance the six class masses

Let

\[
P_L:=\sum_{r:\,P_r\text{ labeled }L}p_r,
\qquad
P_U:=\sum_{r:\,P_r\text{ labeled }U}p_r,
\]

so

\[
P_L+P_U=|P_D|.
\tag{AR.11}
\]

From (AR.9)--(AR.10), the global number of distinct LOWER blockers satisfies

\[
N_L\ge {P_L\over8}-O(1),
\tag{AR.12}
\]

while the global number of distinct UPPER blockers satisfies

\[
N_U\ge {P_U\over16}-O(1).
\tag{AR.13}
\]

Now split at the optimizing mass ratio.

If

\[
P_L\ge {|P_D|\over3},
\]

then

\[
N_L\ge {|P_D|\over24}-O(1).
\tag{AR.14}
\]

Otherwise

\[
P_U>{2|P_D|\over3},
\]

and

\[
N_U>{|P_D|\over24}-O(1).
\tag{AR.15}

Using (AR.7), both cases give

\[
{1\over24}|P_D|
>
\left({s_0\over48}-o(1)\right)D,
\]

which proves (AR.2)--(AR.4).

The `1/3 : 2/3` split is the optimal balance for the conservative multiplicity bounds `P_L/8` and `P_U/16`.

---

## 5. Upper localization doubles its owned input

Assume GLOBAL UPPER. By Section 3, choose the family with an injective owner coordinate for every blocker. The owner lies at an endpoint layer, hence inside the blocker's exact selected-cut interval.

The flexible-scale upper-localization proof uses only:

- linear size of the distinct upper family;
- injective ownership;
- exact interval support;
- the selected-path row count;
- the global angular-defect and terminal-variation budgets.

It does not require the owner coordinates to lie in one residue class.

Thus its input density may be replaced by

\[
\delta_{\rm all}=\beta_*={s_0\over48}.
\tag{AR.16}
\]

The path-specific Oler theorem gives

\[
m\le(A_*+o(1))D,
\qquad
A_*={14\over3\sqrt3}.
\tag{AR.17}
\]

At scale `L=L_D`, the rich-cut/window threshold is

\[
\vartheta_{\rm all}
={\delta_{\rm all}\over3A_*}.
\tag{AR.18}
\]

After the final SIGNED/THIN split, the localized same-type coefficient is

\[
{\vartheta_{\rm all}\over2}
={\delta_{\rm all}\over6A_*}
=c_{\rm all}.
\tag{AR.19}
\]

Since

\[
A_*={14\over3\sqrt3},
\]

we obtain

\[
\begin{aligned}
c_{\rm all}
&={791\over15{,}360{,}000{,}000}
\cdot{\sqrt3\over28}\\
&=
\boxed{
{791\sqrt3\over430{,}080{,}000{,}000}
}\\
&=3.18557521574\ldots\times10^{-9}.
\end{aligned}
\tag{AR.20}

The six-spaced single-class coefficient is

\[
\widehat c_{*,6}
={\gamma_6\over48A_*}
={s_0\over576A_*}.
\]

Equation (AR.20) is

\[
\boxed{
c_{\rm all}=2\widehat c_{*,6}.}
\tag{AR.21}
\]

All defect estimates and train-density conclusions in the scale-free theorem remain unchanged.

---

## 6. Frontier effect

The one-sign strong-TB1 Horn seam can now be organized without choosing one privileged residue class:

```text
all one-sign strong-TB1 coordinates
    -> delete O(1) genuine-upper binary exceptions
    -> run six independent mod-6 Horn systems
    -> aggregate source pairs with multiplicity <= 2

=> either
   > (s0/48-o(1)) D distinct five-row LOWER blockers,

or
   > (s0/48-o(1)) D injectively owned UPPER near-diameters.
```

The implication-forest outcome is no longer a separate global branch; it is simply one source of the UPPER family.

For downstream UPPER work this is a factor-two density gain over retaining one largest mod-six class. At every diverging sublinear localization scale it doubles the guaranteed SIGNED/THIN population without weakening the low-defect train scaffold.

The theorem does not close either metric branch. GLOBAL LOWER still requires local five-row near-unit classification. GLOBAL UPPER still requires metric/order closure of the SIGNED and THIN near-diameter normal forms.

**Disposition:** aggregated all six valid Horn residue systems, removed the global implication-forest branch, proved the equal-density LOWER/UPPER dichotomy `s0/48`, and doubled the flexible-scale UPPER localization coefficient to `3.18557521574...e-9`. C-II and Level I remain open.
