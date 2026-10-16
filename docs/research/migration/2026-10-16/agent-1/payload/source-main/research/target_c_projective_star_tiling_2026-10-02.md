# Target C: projective star intervals asymptotically tile the direction circle

**Date:** 2026-10-02\
**Branch base:** \`research/weighted-cover-stress-concentration-2026-10-02\` at \`369f4674056e523bfc0dc5f4fc7cb944f433e5e3\`\
**Status:** proof-only exact geometric ledger. C-II and Level I remain open.

## 1. Star intervals from the constant-width completion

Let \(H=(B,E_H)\) be the full actual loaded diameter graph. Write

\[
q=|B|,\qquad h=|E_H|,\qquad d_v=\deg_H(v),
\]

and put

\[
\delta_D:=2\arcsin\frac1{2D}.
\tag{1}
\]

For each actual diameter vertex \(v\) with \(d_v\ge2\), let \(I_v\) be the open
support-normal interval forced by its diameter star in the constant-width
completion used by the current cubic-star theorem. Write

\[
\Theta_v:=|I_v|.
\]

That theorem proves:

1. every pair of consecutive diameter-partner rays at \(v\) is separated by at least
   \(\delta_D\), so
   \[
   \Theta_v\ge(d_v-1)\delta_D;
   \tag{2}
   \]
2. for distinct diameter vertices \(v,w\), the four intervals
   \[
   I_v,\ I_v+\pi,\ I_w,\ I_w+\pi
   \]
   have pairwise disjoint interiors.

The second statement implies that the projective images

\[
\bar I_v\subset\mathbb R/\pi\mathbb Z
\]

are pairwise interior-disjoint. Hence

\[
\boxed{
\sum_{v:d_v\ge2}\Theta_v\le\pi.
}
\tag{3}
\]

No contact graph input is used here.

## 2. Exact star-tiling defect ledger

Define the internal star gap excess

\[
X_v
:=
\Theta_v-(d_v-1)\delta_D
\ge0.
\tag{4}
\]

Let

\[
G_{\rm star}
:=
\pi-\sum_{v:d_v\ge2}\Theta_v
\ge0
\tag{5}
\]

be the total projective measure not covered by the diameter-star support intervals.

Every loaded diameter vertex has positive diameter degree. Therefore

\[
\sum_{v:d_v\ge2}(d_v-1)
=
\sum_{v\in B}(d_v-1)
=
2h-q.
\tag{6}
\]

Substitute (4) into (5):

### Theorem 2.1 -- exact projective star-tiling ledger

\[
\boxed{
G_{\rm star}
+
\sum_{v:d_v\ge2}X_v
=
\pi-(2h-q)\delta_D.
}
\tag{7}
\]

Every term on the left is nonnegative. Consequently

\[
\boxed{
(2h-q)\delta_D\le\pi.
}
\tag{8}
\]

The gain over the ordinary diameter-direction packing inequality is that (7) separates
the global deficit into:

- actual uncovered projective direction measure \(G_{\rm star}\);
- excess spacing inside the stars themselves.

## 3. Low-detour square-root branch

Assume

\[
x_B=o(D),
\qquad
\nu(H)=O(\sqrt D).
\tag{9}
\]

Current main gives the near-circle loaded-hull endpoint

\[
\frac qD\to\pi.
\tag{10}
\]

Woodall gives

\[
d_H:=q-h\le\nu=o(D).
\tag{11}
\]

Hence

\[
h=q-o(D)=\pi D-o(D)
\tag{12}
\]

and

\[
2h-q=q-2d_H=\pi D-o(D).
\tag{13}
\]

Since

\[
\delta_D=\frac1D+O(D^{-3}),
\tag{14}
\]

equation (13) gives

\[
(2h-q)\delta_D=\pi-o(1).
\tag{15}
\]

Apply Theorem 2.1:

\[
\boxed{
G_{\rm star}=o(1),
\qquad
\sum_vX_v=o(1).
}
\tag{16}
\]

Thus the projective direction circle is asymptotically tiled by actual
diameter-star support intervals, and the total excess over minimum
\(\delta_D\)-spacing inside those intervals also vanishes.

This statement is independent of the good-side normal-cone ledger. The latter uses
loaded-hull unit sides and turning angles; (16) uses only the full actual diameter
graph, the constant-width support intervals, and the low-detour density endpoint.

## 4. Quantitative consequence for the square-root carrier sea

The companion balanced-carrier theorem gives a set \(\mathcal M_D\) of medium
leaf-carrying vertices satisfying

\[
|\mathcal M_D|\ge c_0\sqrt D-o(\sqrt D)
\tag{17}
\]

for an explicit \(c_0>0\), and

\[
a\sqrt D\le d_v\le b\sqrt D
\qquad(v\in\mathcal M_D)
\tag{18}
\]

for fixed positive \(a,b\).

Hence every medium star has natural interval scale

\[
(d_v-1)\delta_D=\Theta(D^{-1/2}).
\tag{19}
\]

Fix \(\varepsilon>0\). From (16),

\[
\#\left\{
v\in\mathcal M_D:
X_v>\frac{\varepsilon}{\sqrt D}
\right\}
\le
\frac{\sqrt D}{\varepsilon}\sum_vX_v
=
o(\sqrt D).
\tag{20}
\]

Therefore all but \(o(\sqrt D)\) medium carriers satisfy

\[
\boxed{
\Theta_v
=
(d_v-1)\delta_D+o(D^{-1/2}).
}
\tag{21}
\]

This recovers the internal near-minimal spacing part of the companion normal-cone
theorem without using good hull sides.

## 5. Inter-star projective gaps are small for almost every carrier

Order the nonempty projective star intervals cyclically:

\[
\bar I_1,\ldots,\bar I_m.
\]

Let \(g_j\ge0\) be the projective gap from the end of \(\bar I_j\) to the beginning
of \(\bar I_{j+1}\). Then

\[
\sum_{j=1}^m g_j=G_{\rm star}=o(1).
\tag{22}
\]

The balanced carrier theorem and the cubic incidence lower bound give

\[
m=\Theta(\sqrt D)
\tag{23}
\]

in the hard near-circle regime.

For any fixed \(\varepsilon>0\),

\[
\#\left\{
j:g_j>\frac{\varepsilon}{\sqrt D}
\right\}
\le
\frac{\sqrt D}{\varepsilon}G_{\rm star}
=
o(\sqrt D).
\tag{24}
\]

Thus a full-density subfamily of star boundaries has

\[
\boxed{
g_j=o(D^{-1/2}).
}
\tag{25}
\]

Intersecting with the medium-carrier subfamily from Section 4 shows that a positive
\(\sqrt D\)-population of actual leaf-carrying stars has simultaneously

\[
\Theta_v=\Theta(D^{-1/2}),
\qquad
X_v=o(D^{-1/2}),
\tag{26}
\]

and neighboring projective star gaps

\[
o(D^{-1/2}).
\tag{27}
\]

The star sea is therefore not merely a collection of \(\Theta(\sqrt D)\) broad
packets. At its natural square-root scale it is an asymptotic partition of the
projective direction circle.

## 6. Inverse-phase windows see only one local star boundary pattern

Section 90 uses reduced phase windows of width

\[
W_D=O(D^{-1}).
\tag{28}
\]

This is much smaller than the typical medium-star scale \(D^{-1/2}\).

Fix one such window \(J_D\). Because the projective star intervals are pairwise
interior-disjoint, exactly one of the following occurs:

1. \(J_D\) is contained in one star interval;
2. \(J_D\) meets one or more star boundaries / uncovered gaps.

The current narrow-bin multiplicity theorem already bounds the number of stars that
can straddle \(J_D\) by an absolute constant. The new ledger adds that, away from
\(o(\sqrt D)\) exceptional star boundaries, the local geometry around such a boundary
has no square-root-scale empty angular gap: adjacent medium-star intervals meet to
\(o(D^{-1/2})\).

This does **not** force single-star Section-157 bracing. A star interval can contain
the train phase while none of its diameter edges crosses the train shore cut.
Consequently split-star witnesses can still come from stars on opposite sides of the
phase. The remaining issue is shore incidence, not projective availability.

## 7. Laminar shore cuts: one carrier contributes a nested contiguous leaf subblock

Let \(a\) be a leaf-carrying diameter vertex, with its degree-one partners in one
consecutive loaded-hull block

\[
L(a)=\{p_1,\ldots,p_t\}
\]

as proved by the current leaf-fan theorem.

Let \(\tau\) be a proper outer-to-outer train crosscut. Its two shores meet the outer
boundary in complementary boundary arcs. Exactly one of those arcs avoids the carrier
\(a\). Because \(L(a)\) also avoids \(a\), identify the circle minus \(a\) with a
line. Both the leaf block and the boundary arc opposite \(a\) are intervals in this
linear order. Therefore their intersection is an interval.

Hence:

### Lemma 7.1 -- active leaf subblock

For one O--O cut \(\tau\), the pendant diameter edges at \(a\) that cross \(\tau\)
form one consecutive subblock of the leaf order

\[
ap_1,\ldots,ap_t.
\tag{29}
\]

Now take a laminar path of O--O cuts and restrict to cuts lying on one side of the
complement region containing \(a\). Their opposite boundary arcs are nested.
Therefore the active pendant subblocks at \(a\) are nested as well.

In particular each leaf edge can enter or leave the active subblock at most once along
that one-sided cut path, and the two active-subblock endpoints move monotonically
through the ordered leaf block.

This is the precise shore-incidence structure available for the split-star problem.

## 8. Why this still does not close the diffuse split-star branch

A medium carrier has \(\Theta(\sqrt D)\) pendant leaf edges. By Lemma 7.1 it can
therefore change its active subblock only \(O(\sqrt D)\) times along one laminar
shore. Since the hard branch has \(\Theta(\sqrt D)\) medium carriers, the total
available star-boundary switching capacity is still \(O(D)\).

That matches the linear split-star population left by the October 1 fixed-pair
concentration theorem. Thus the new monotonicity is quantitatively sharp at the
counting level:

\[
\Theta(\sqrt D)\text{ carriers}
\times
\Theta(\sqrt D)\text{ possible leaf transitions per carrier}
=
\Theta(D).
\tag{30}
\]

A closing split-star theorem must use more than support counts. It must exploit at
least one of:

- the near-minimal projective spacing (16), (21), (25);
- the exact KKT cut resultants;
- the complete crossing order of the two Section-90 train shores;
- or finite diameter feasibility of the laminar shear.

**Disposition:** proof-only exact/star-order reduction. No computation, numerical
search, verifier execution, or CI output is used.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/weighted-cover-stress-concentration-2026-10-02` at exact source tip `ab10eeda2bc16a36daacd54be7cb2cbfdeb1fe1f`. No original PR is associated with the source branch. This report remains a proof-only, unreviewed Target C-II candidate; its stated KKT and train hypotheses are not promoted, and it does not close C-II or Level I. No verifier or computational certificate was present in the source lineage.
