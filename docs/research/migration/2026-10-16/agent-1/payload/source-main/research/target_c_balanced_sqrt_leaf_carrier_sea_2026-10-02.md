# Target C: balanced square-root sea of diameter-leaf carriers

**Date:** 2026-10-02\
**Base:** October Woodall leaf/fan stack plus the global cubic star moment\
**Status:** proof-only structural consequence. C-II and Level I remain open.

## 1. Carrier notation

Let \(H\) be the full actual diameter graph. Write

\[
h=|E(H)|,\qquad \nu=\nu(H).
\]

Let \(\mathcal C\) be the set of nonleaf diameter vertices that have at least one
degree-one diameter neighbor. For \(v\in\mathcal C\), put

\[
t_v:=\#\{\text{degree-one diameter neighbors of }v\},
\qquad
c:=|\mathcal C|,
\qquad
P:=\sum_{v\in\mathcal C}t_v.
\tag{1}
\]

Thus \(P\) is the number of pendant diameter edges whose other endpoint is a
nonleaf carrier. Isolated \(K_2\) diameter components are not counted in \(P\).

Current Woodall bookkeeping gives

\[
\boxed{c\le\nu}
\tag{2}
\]

by choosing one pendant edge at each carrier, and in the square-root hard regime it
also gives

\[
\boxed{P\ge h-2\nu-O(1).}
\tag{3}
\]

In the forest branch the \(O(1)\) can be omitted; in the cyclic branch it is harmless
and disappears asymptotically.

## 2. The carrier set itself obeys the cubic incidence theorem

Apply the current-main cubic incidence theorem to

\[
S=\mathcal C
\]

and to the specified family of the \(P\) pendant diameter edges counted in (1).
Every such edge has exactly one endpoint in \(\mathcal C\), so the incidence count
on \(S\) is exactly

\[
J=P.
\]

Therefore

\[
\boxed{
(P-c)_+^3<\mathcal B_Dc^2,
}
\tag{4}
\]

where

\[
\frac{\mathcal B_D}{D^2}\to12\pi\sqrt3.
\tag{5}
\]

This is stronger structurally than applying the same incidence theorem to an
arbitrary minimum vertex cover: it counts actual leaf-carrying centers.

## 3. Density-sensitive carrier lower bound

Suppose along a subsequence

\[
\frac PD\to y>0
\]

and

\[
c=O(\sqrt D).
\]

Then \(c/D\to0\), so dividing (4) by \(D^3\) gives

\[
y^3
\le
12\pi\sqrt3\,
\liminf\frac{c^2}{D}.
\]

Hence

\[
\boxed{
\liminf\frac c{\sqrt D}
\ge
\frac{y^{3/2}}{\sqrt{12\pi\sqrt3}}.
}
\tag{6}
\]

### Near-circle square-root specialization

Assume

\[
x_B=o(D),\qquad
\nu=O(\sqrt D).
\tag{7}
\]

The near-circle theorem gives \(q/D\to\pi\). Woodall gives
\(d_H=q-h\le\nu=o(D)\), hence

\[
h=\pi D-o(D).
\tag{8}
\]

Equation (3) then gives

\[
P=\pi D-o(D).
\tag{9}
\]

Thus (6) becomes

\[
\boxed{
\liminf\frac c{\sqrt D}
\ge
\frac{\pi}{\sqrt{12\sqrt3}}
=
0.689\ldots .
}
\tag{10}
\]

Together with \(c\le\nu=O(\sqrt D)\),

\[
\boxed{c=\Theta(\sqrt D).}
\tag{11}
\]

So the hard near-circle branch cannot consist of one or finitely many giant
Reuleaux stars. It has square-root many actual leaf-carrying centers.

## 4. Third-moment stability: many carriers have square-root order

The global cubic star theorem gives

\[
\sum_{v}(d_H(v)-1)^3
<
12\pi\sqrt3\,D^2.
\tag{12}
\]

For a carrier with at least one nonleaf/core incident diameter edge,

\[
d_H(v)-1\ge t_v.
\]

For a star-component carrier with no core edge,

\[
d_H(v)-1=t_v-1.
\]

Thus uniformly, with

\[
u_v:=(t_v-1)_+,
\]

we have

\[
\boxed{
\sum_{v\in\mathcal C}u_v^3
<
C_3D^2,
\qquad
C_3:=12\pi\sqrt3.
}
\tag{13}
\]

Also

\[
\sum_{v\in\mathcal C}u_v
\ge
P-c
=
\pi D-o(D)
\tag{14}
\]

under (7).

Now fix a hard-regime upper constant \(K<\infty\) such that

\[
\nu\le K\sqrt D
\]

along the subsequence. By (2),

\[
c\le K\sqrt D.
\tag{15}
\]

Define

\[
a_K:=\frac{\pi}{4K},
\qquad
B_*:=\sqrt{48\sqrt3}.
\tag{16}
\]

Call a carrier **medium** when

\[
a_K\sqrt D
\le u_v\le
B_*\sqrt D.
\tag{17}
\]

### Theorem 4.1 -- balanced carrier population

Along every near-circle sequence satisfying (7),

\[
\boxed{
\#\{v\in\mathcal C:
a_K\sqrt D\le u_v\le B_*\sqrt D\}
\ge
\left(\frac{\pi}{2B_*}-o(1)\right)\sqrt D.
}
\tag{18}
\]

Numerically,

\[
B_*=9.11\ldots,
\qquad
\frac{\pi}{2B_*}=0.172\ldots .
\]

### Proof

The total \(u\)-mass on carriers with

\[
u_v<a_K\sqrt D
\]

is at most

\[
c\,a_K\sqrt D
\le
K\sqrt D\cdot{\pi\over4K}\sqrt D
=
{\pi\over4}D.
\tag{19}
\]

For carriers with

\[
u_v>B_*\sqrt D,
\]

we have

\[
u_v
<
\frac{u_v^3}{B_*^2D}.
\]

Using (13),

\[
\sum_{u_v>B_*\sqrt D}u_v
<
\frac{C_3D^2}{B_*^2D}
=
\frac{12\pi\sqrt3}{48\sqrt3}D
=
{\pi\over4}D.
\tag{20}
\]

By (14), the medium carriers therefore carry at least

\[
{\pi\over2}D-o(D)
\tag{21}
\]

total \(u\)-mass. Each medium carrier contributes at most \(B_*\sqrt D\), so their
number is at least

\[
\frac{(\pi/2)D-o(D)}{B_*\sqrt D}
=
\left(\frac{\pi}{2B_*}-o(1)\right)\sqrt D.
\]

QED.

Thus a positive square-root population of carriers each supports a positive
square-root population of diameter leaves.

## 5. Geometric meaning in the low-detour fan branch

Current main proves that the degree-one neighbors of one carrier form one consecutive
loaded-hull block, and that when \(x_B=o(D)\) almost every internal block adjacency is
an actual unit hull contact.

Therefore each medium carrier from Theorem 4.1 supports, up to the \(o(D)\) global
bad-adjacency budget, a radius-\(D\) leaf block of order

\[
\Theta(\sqrt D)
\]

whose successive good chords are exactly unit length.

The hard endpoint is consequently a genuine two-scale structure:

\[
\boxed{
\Theta(\sqrt D)\text{ macroscopic carrier blocks}
\times
\Theta(\sqrt D)\text{ exact leaf contacts per typical block}.
}
\tag{22}
\]

This is the same square-root-by-square-root scale suggested by the abstract star
regression in the cubic-budget report, but now it is forced inside the actual
near-circle source rather than merely numerically compatible.

## 6. Phase-bin implication

A medium carrier has star order \(\Theta(\sqrt D)\). Consecutive incident diameter
directions are separated by \(\Theta(1/D)\), so its projective star interval has
width

\[
\Theta(D^{-1/2}).
\tag{23}
\]

The Section-90 phase bins have width \(O(D^{-1})\). Hence one medium star spans
\(\Theta(\sqrt D)\) such inverse-\(D\) bins.

This does not by itself force single-star train bracing: an outer-to-outer cut may
place all partners of that carrier on one shore. It does show that the remaining
split-star mechanism lives inside a direction circle partitioned into
\(\Theta(\sqrt D)\) broad star intervals, each much wider than one phase bin.

A closing train theorem should exploit cut support/order inside this forced
square-root star sea, not merely the number of available diameter vertices.

**Disposition:** proof-only structural reduction. No computation, numerical search,
verifier, or CI output is used.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/weighted-cover-stress-concentration-2026-10-02` at exact source tip `ab10eeda2bc16a36daacd54be7cb2cbfdeb1fe1f`. No original PR is associated with the source branch. This report remains a proof-only, unreviewed Target C-II candidate; its stated KKT and train hypotheses are not promoted, and it does not close C-II or Level I. No verifier or computational certificate was present in the source lineage.
