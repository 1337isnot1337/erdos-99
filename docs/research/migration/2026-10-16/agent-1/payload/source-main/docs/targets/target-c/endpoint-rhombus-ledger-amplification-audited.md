# Target C — audited endpoint rhombus/ledger amplification, normalized §§148–150

**Date:** 2026-09-12  
**Lifecycle:** audited-working proof-only route module; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module is the clean replacement for the collision-heavy research tail formerly
carried by PR #393. It depends on the already-normalized joint-payment / diameter-moment
chain §§134–140 and preserves only the genuinely new results that survived hostile
review.

The historical `h/D` corollaries below are recorded for provenance, but they are not the
current scalar frontier: normalized §146 gives the stronger Type-II diameter-edge floor
`liminf h/D >= 1.8195135379794445...`. The new value here is in the **weighted defect
inequalities**, which retain information about `d_H` and `s_Z` that an `h`-only floor
does not.

No withdrawn unconditional `q-k` or nonmatching/interface floor is used.

---

# §148 — component-ledger amplification of the endpoint diameter moment

Use canonical Section 75 notation. For each unloaded positive-contact component `I_r`,
let

- `delta_r` be its contact-graph diameter;
- `P_r=conv(A_r)` be its harmonic attachment cell; and
- `d_r=diam(P_r)`.

Let

\[
k:=d_H+s_Z,
\]

and in sufficiently large Type II let `m` be the number of nonunit sides of the loaded
force hull. The centralized Type-II loaded-contact theorem gives

\[
e_{BB}=q-m.
\tag{148.1}
\]

The exact pinned/component identity is

\[
c_I+s_C=m+k-2.
\tag{148.2}
\]

Then one has the finite inequality

\[
\boxed{
q+m-k\ge \sum_r d_r-2.
}
\tag{148.3}
\]

## 148.1 Proof of the finite inequality

Canonical harmonic localization gives

\[
d_r\le\delta_r+2,
\]

hence

\[
\sum_r d_r\le\sum_r\delta_r+2c_I.
\tag{148.4}
\]

Canonical Section 75 gives the exact all-phase component ledger

\[
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C,
\tag{148.5}
\]

with `R_I,s_B>=0`. Therefore

\[
\sum_r\delta_r\le6+e_{BB}+2s_C-3k.
\tag{148.6}
\]

Insert (148.1)–(148.2) into (148.4)–(148.6):

\[
\begin{aligned}
\sum_r d_r
&\le 6+(q-m)+2(m+k-2-c_I)-3k+2c_I\\
&=q+m-k+2.
\end{aligned}
\]

This proves (148.3). The `c_I` cancellation is exact; no asymptotic estimate on the
number of harmonic components is needed for the finite theorem.

## 148.2 Endpoint consequence

The repaired normalized §140 complement-gap theorem gives, on the Section-118
endpoint/common-cap branch,

\[
\sum_r d_r\ge(S_*-o(1))D,
\qquad
S_*:=2.798596312209462\ldots .
\tag{148.7}
\]

Thus

\[
\boxed{
q+m-k\ge S_*D-o(D).
}
\tag{148.8}
\]

Normalized §140 also gives

\[
3q-2m-5k
\ge(S_*+c_*)D-o(D),
\qquad
c_*:={\pi\over4}(2-\sqrt3)
=0.210446803619233\ldots .
\tag{148.9}
\]

Twice (148.8) plus (148.9) eliminates `m`:

\[
\boxed{
5q-7k
\ge(3S_*+c_*)D-o(D)
=8.60623574024762\ldots D-o(D).
}
\tag{148.10}
\]

Since `q=h+d_H` and `k=d_H+s_Z`,

\[
\boxed{
5h-2d_H-7s_Z
\ge8.60623574024762\ldots D-o(D).
}
\tag{148.11}
\]

Discarding the nonnegative defect terms gives the weaker historical corollary
`h/D>=1.72124714804952...`; this scalar corollary is now dominated by §146 and should
not be cited as the frontier. The weighted inequality (148.11) is the retained result.

**Hostile-audit disposition:** PASS. No source point is deleted, no core affine-kernel
statement is extended to contact isolates, and no rejected interface floor enters the
proof.

---

# §149 — cellwise strict-rhombus boundary payment

For one harmonic component `I_r`, let

- `H_r` be its actual induced harmonic plane graph;
- `R_{4,r}` be the number of bounded quadrilateral faces of `H_r`;
- `L_r` be the occurrence-counted outer-face walk length; and
- `P_{exc,r}` be the total boundary degree of bounded nonquadrilateral faces.

Canonical Section 82 makes every bounded quadrilateral face of `H_r` a strict unit
rhombus. Apply the canonical strict-rhombus boundary theorem to this local finite
collection. If `B_{4,r}` is its physical boundary-edge occurrence count, then

\[
B_{4,r}\ge4\sqrt{R_{4,r}}.
\tag{149.1}
\]

Every occurrence counted by `B_{4,r}` has a quadrilateral on one side and either the
outer face or a bounded nonquadrilateral face on the other. Therefore

\[
B_{4,r}\le L_r+P_{exc,r},
\]

so

\[
\boxed{
L_r+P_{exc,r}\ge4\sqrt{R_{4,r}}.
}
\tag{149.2}
\]

Bridges and repeated outer vertices are harmless because `L_r` is occurrence-counted.

## 149.1 Exact global upper payment

Normalized §134 gives

\[
\sum_r(L_r+P_{exc,r}-2a_r)
\le10(e_{BB}-k-d_{tile})-6C_A.
\tag{149.3}
\]

The exact attachment-incidence identity is

\[
a:=\sum_ra_r
=3q-6-2(e_{BB}-k)-2s_C-d_{tile}.
\tag{149.4}
\]

Hence

\[
\sum_r(L_r+P_{exc,r})
\le6(q-k)+6e_{BB}-4s_C-12d_{tile}-6C_A-12.
\tag{149.5}
\]

Normalized §137 proves the completion-triangle inequality

\[
e_{BB}-C_A\le2d_{tile}.
\tag{149.6}
\]

Thus

\[
6e_{BB}-6C_A-12d_{tile}\le0,
\]

and

\[
\boxed{
\sum_r(L_r+P_{exc,r})
\le6(q-k)-4s_C-12.
}
\tag{149.7}
\]

Sum (149.2) and compare with (149.7):

\[
\boxed{
3(h-s_Z)-2s_C
\ge2\sum_r\sqrt{R_{4,r}}+6.
}
\tag{149.8}
\]

This is the main theorem. It is sensitive to how the quadratic rhombus population is
split among harmonic cells.

## 149.2 Coarse Type-II check

Every global strict-rhombus face with no loaded vertex belongs to one unloaded component
and remains a bounded quadrilateral face of its `H_r`. A loaded positive-contact vertex
has degree at most three, so at most `O(q)=O(D)` global quadrilateral faces touch the
loaded set. Therefore

\[
\sum_rR_{4,r}\ge R_4-O(D).
\tag{149.9}
\]

In Type II,

\[
{R_4\over D^2}\to
\Delta_2:={\pi\over2\sqrt3}.
\]

Since `sum sqrt(x_i)>=sqrt(sum x_i)` for nonnegative terms,

\[
\liminf {1\over D}\sum_r\sqrt{R_{4,r}}
\ge\sqrt{\Delta_2}.
\]

Thus (149.8) implies only the valid tradeoff

\[
\boxed{
\liminf {3(h-s_Z)-2s_C\over D}
\ge2\sqrt{\Delta_2}
=1.9046256137\ldots .
}
\tag{149.10}
\]

This must **not** be rewritten as an unconditional `(q-k)/D>=1.9046256...` floor. The
negative pinned-surplus term is essential.

## 149.3 Partition refinement

For disjoint groups of harmonic components `G_1,...,G_t`, if

\[
\sum_{r\in G_j}R_{4,r}
\ge(\rho_j-o(1))D^2,
\]

then (149.8) gives

\[
\boxed{
\liminf {3(h-s_Z)-2s_C\over D}
\ge2\sum_{j=1}^t\sqrt{\rho_j}.
}
\tag{149.11}
\]

No numerical group decomposition is asserted without separately proving the groupwise
quadratic rhombus-count floors.

**Hostile-audit disposition:** PASS. The constant `+6`, the occurrence bookkeeping,
and the completion-triangle cancellation have been independently recomputed.

---

# §150 — endpoint partition amplification

This section is specific to the repaired Section-118/§140 endpoint/common-cap branch.
It combines the partition-sensitive theorem §149 with four disjoint macroscopic regions:

1. the wrapping harmonic carrier; and
2. the three principal complement-gap segments.

Let

\[
\theta_*=2.704779235215494\ldots,
\qquad
\sigma_*=0.0088,
\]

\[
\phi_*:=2\pi-2\theta_*
=0.873626836748598\ldots,
\]

\[
G(t):={t-\sin t\over8},
\qquad
a_0={\sqrt3\over2}.
\]

The sharp Section-118 companion supplies the conservative wrapping-group area floor

\[
A_*=0.4703752868004241\ldots .
\tag{150.1}
\]

It also gives the principal-gap lower bounds

\[
g_1\ge\theta_*-{10\over3}\sigma_*+o(1),
\qquad
g_2,g_3\ge\phi_*+o(1).
\tag{150.2}
\]

Define

\[
\boxed{
B_*:={2\over\sqrt{a_0}}
\left[
\sqrt{A_*}
+\sqrt{G(\theta_*-10\sigma_*/3)}
+2\sqrt{G(\phi_*)}
\right].
}
\tag{150.3}
\]

Numerically,

\[
\boxed{B_*=3.10463675756624\ldots .}
\tag{150.4}
\]

Then every endpoint/common-cap survivor satisfies

\[
\boxed{
3(h-s_Z)-2s_C
\ge(B_*-o(1))D.
}
\tag{150.5}
\]

## 150.1 Area-to-rhombus conversion is groupwise

Canonical Section 68 writes every global strict-rhombus area as

\[
area(R)=a_0+\epsilon_R,
\qquad
\epsilon_R\ge0,
\]

with

\[
\sum_R\epsilon_R=O(D).
\tag{150.6}
\]

Hence any selected unloaded-only rhombus family with total area `(A+o(1))D^2` has
cardinality

\[
\left({A\over a_0}+o(1)\right)D^2.
\tag{150.7}
\]

Canonical Section 83 gives the nonnegative local filling deficit

\[
\sum_r\bigl(area(P_r)-A_{4,r}\bigr)=o(D^2),
\tag{150.8}
\]

where `A_{4,r}` is the unloaded-only strict-rhombus area belonging to `I_r`. Because
each summand is nonnegative, **any selected cell group** inherits at most `o(D^2)`
filling loss.

For the fixed wrapping cell, (150.1) and (150.8) therefore give

\[
R_{4,w}
\ge\left({A_*\over a_0}-o(1)\right)D^2.
\tag{150.9}
\]

For a fixed principal gap `g_j`, the repaired §140 fixed-gap area-saturation argument
uses the order `D->infinity` followed by the positive-area cutoff `eta->0`. The residual
cells assigned to that gap carry total cell area

\[
(G(g_j)-o(1))D^2.
\]

Their summed local filling deficit is bounded by (150.8), so their unloaded-only
rhombus area has the same leading coefficient. Thus for a synchronized finite set of
the three fixed gaps there are disjoint groups `G_j` with

\[
\sum_{r\in G_j}R_{4,r}
\ge\left({G(g_j)\over a_0}-o(1)\right)D^2.
\tag{150.10}
\]

The groups are disjoint from one another and from the wrapping cell: one positive-area
convex residual cell cannot occupy two different components of the disk minus the
wrapping convex hull.

## 150.2 Apply §149 group by group

Retain only the wrapping group and the three principal-gap groups in (149.8). For each
gap group,

\[
\sum_{r\in G_j}\sqrt{R_{4,r}}
\ge\sqrt{\sum_{r\in G_j}R_{4,r}}.
\]

Equations (150.9)–(150.10) give

\[
\liminf {3(h-s_Z)-2s_C\over D}
\ge
{2\over\sqrt{a_0}}
\left[
\sqrt{A_*}+\sum_{j=1}^3\sqrt{G(g_j)}
\right].
\tag{150.11}
\]

Use (150.2) and monotonicity of `G` on `[0,pi]` to obtain (150.5). The regression
values are

\[
G(\theta_*-10\sigma_*/3)=0.278249800512664\ldots,
\]

\[
G(\phi_*)=0.0133705313996309\ldots .
\]

## 150.3 Combine with §148

Canonical Section 75 gives `c_I=o(D)`, and (148.2) implies

\[
s_C=m+k+o(D).
\]

Thus (150.5) becomes

\[
\boxed{
3q-2m-5k\ge B_*D-o(D).
}
\tag{150.12}
\]

Twice the component-ledger inequality (148.8),

\[
q+m-k\ge S_*D-o(D),
\]

plus (150.12) eliminates `m`:

\[
\boxed{
5q-7k
\ge(2S_*+B_*)D-o(D)
=8.70182938198516\ldots D-o(D).
}
\tag{150.13}
\]

Equivalently,

\[
\boxed{
5h-2d_H-7s_Z
\ge8.70182938198516\ldots D-o(D).
}
\tag{150.14}
\]

Discarding the defect terms gives the historical scalar corollary
`h/D>=1.74036587639703...`; as noted at the top, this scalar floor is dominated by
normalized §146. The weighted inequality (150.14) is the surviving structural result.

---

# Final hostile-audit disposition

**§148 PASS.** The component ledger is finite, the `c_I` terms cancel exactly, and the
endpoint insertion uses the repaired §140 diameter moment rather than the rejected
exact-full-gap-cell shortcut.

**§149 PASS.** Local strict-rhombus boundaries are occurrence-counted; unloaded-only
global rhombi transfer to local quadrilateral faces; loaded-touching rhombi are only
`O(D)`; and the global upper payment uses the valid §137 completion-triangle
cancellation.

**§150 PASS.** Section 83's local filling deficits are nonnegative, so any selected
macroscopic group inherits `o(D^2)` filling loss. The three fixed gap groups are handled
with the repaired §140 order of limits. Section 68's global `O(D)` rhombus-area excess
is strong enough for groupwise area-to-count conversion.

The h-only consequences of §§148 and 150 are no longer the quantitative frontier because
§146 is stronger. The weighted inequalities remain useful and are not implied by an
h-only lower bound.

No source point is removed or reclassified; contact isolates remain outside the
positive-contact harmonic decomposition exactly as in the canonical route. No theorem
above closes the macroscopic inactive-container branch or constructs a same-cardinality
strict sub-`D` competitor.

**Overall verdict:** PASS at audited-working proof-only scope with the stated endpoint
hypotheses. Canonical theorem-state authority is unchanged; C-II and Level I remain
open.
