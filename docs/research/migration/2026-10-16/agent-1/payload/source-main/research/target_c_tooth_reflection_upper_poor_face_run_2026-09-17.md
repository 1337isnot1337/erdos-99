# Target C-II — the upper-poor FREE branch forces one deep inactive face run

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only consequence of the two-boundary slack tradeoff  
**Scope:** non-anchored FREE reflection modules, all-inactive ancestry, upper-poor side of the scale tradeoff  
**Dependencies:** two-sided inactive gate absorption; two-boundary slack tradeoff; inactive-chain contact-crossing threshold  
**Certificate:** `research/verify_target_c_tooth_reflection_upper_poor_face_run_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The two-boundary tradeoff gives a long consecutive run of lower gates when the ancestry has few upper gates. A stronger choice of run makes that branch geometric: one run carries a proportional share of the entire support traverse, lies in one original contact face, and becomes an exact support-monotone unit chain in the activation deformation.

Let an all-inactive ancestry reach the near-opposite threshold. Write

\[
A=a_{z_m}-a_{z_0}>D-O(\sqrt D),
\]

let `U` be the number of upper-gate edges, and fix an integer scale

\[
1\ll M=M_D\ll D.
\]

Assume the upper-poor case

\[
U<M.
\tag{FR.1}
\]

Then there is one consecutive all-lower ancestry run `R` such that

\[
\boxed{
\operatorname{span}_N(R)
\ge
\frac{D-O(\sqrt D)}{M}.
}
\tag{FR.2}
\]

Every vertex of this run is fully inactive in the original source, every original run edge has length below `sqrt(3)` for large `D`, and the whole run lies in one face of the original unit-contact graph. Since `D/M -> infinity`, that face is not an ordinary quadrilateral grain. It is a bounded exceptional face or the outer contact face.

The run also satisfies

\[
\boxed{
|E(R)|
\ge
\frac{D-O(\sqrt D)}{M}-O(1),
}
\tag{FR.3}
\]

and contains a vertex-disjoint matching of size

\[
\boxed{
\frac{D-O(\sqrt D)}{4M}-O(1)
}
\tag{FR.4}

of original fully inactive pairs with

\[
\boxed{
1<|x-y|
\le
1+(2h_*+o(1))\frac{M}{D},
\qquad
h_*={\sqrt{303}\over52}.
}
\tag{FR.5}

At the terminal activation configuration, before strictification, the complete run is an exact unit-contact chain, every edge has nonnegative `N`-projection, and its total forward `N`-progress is still

\[
\boxed{
\frac{D-O(\sqrt D)}{M}-O(1).
}
\tag{FR.6}

Thus the upper-poor branch cannot distribute its near-unit burden among many unrelated parts of the source. A single exceptional/outer contact face carries an expanding, support-monotone inactive ladder.

---

## 1. Lower gates carry essentially the whole support traverse

For an ancestry edge use the event vector

\[
d_j=z_j-\Delta_jN-z_{j+1},
\qquad
\Delta_j=s_{j+1}-s_j>0.
\]

For a lower gate, the first-hit sign gives

\[
|d_j|=1,
\qquad
N\cdot d_j\ge0,
\]

so its original support-depth gain is

\[
g_j:=a_{z_{j+1}}-a_{z_j}
=N\cdot d_j+\Delta_j>0.
\tag{FR.7}
\]

For an upper gate,

\[
|d_j|=D,
\qquad
N\cdot d_j<0,
\]

and therefore

\[
g_j=N\cdot d_j+\Delta_j<\Delta_j.
\tag{FR.8}
\]

Let

\[
G_{\rm low}:=\sum_{j\in E_{\rm low}}g_j,
\qquad
G_{\rm up}:=\sum_{j\in E_{\rm up}}g_j.
\]

The activation times telescope:

\[
\sum_j\Delta_j\le t_D<h_*+D^{-1/3}=O(1).
\tag{FR.9}
\]

Hence (FR.8) gives

\[
G_{\rm up}<\sum_{j\in E_{\rm up}}\Delta_j\le t_D.
\]

Since `A=G_low+G_up`,

\[
\boxed{
G_{\rm low}>A-t_D>D-O(\sqrt D).
}
\tag{FR.10}

So upper gates may jump backward by a large amount, but they cannot pay any macroscopic positive fraction of the required inward support traverse. Almost all positive support progress is carried by lower gates.

---

## 2. One consecutive lower run has support span `Omega(D/M)`

Deleting the `U` upper edges partitions all lower edges into at most

\[
U+1\le M
\]

consecutive all-lower runs.

Because every lower gain in (FR.7) is positive, the support span of a run is exactly the sum of its lower gains. Equation (FR.10) and pigeonhole therefore give one run `R` with

\[
\operatorname{span}_N(R)
\ge {G_{\rm low}\over U+1}
\ge {D-O(\sqrt D)\over M},
\]

which proves (FR.2).

This choice is stronger than choosing merely the longest lower run: it forces the selected run to advance deeply in the canonical reflection support direction.

---

## 3. The selected run is a simple path inside one original contact face

For every lower edge,

\[
z_j-z_{j+1}=d_j+\Delta_jN,
\qquad |d_j|=1,
\]

so

\[
|z_j-z_{j+1}|
\le1+\Delta_j
\le1+t_D
<1+h_*+o(1).
\tag{FR.11}
\]

Numerically,

\[
1+h_*=1.334747984337100\ldots<\sqrt3.
\tag{FR.12}
\]

The sharp contact-crossing lemma says that any source segment crossing a unit contact edge has length at least `sqrt(3)`. Hence no edge of `R` crosses the original contact graph. It also cannot pass through a third source vertex, because its length is below two while source points are unit-separated.

Every run vertex is fully inactive in the original source and therefore lies in the interior of a contact face. Consecutive run endpoints lie in the same face, so the entire run lies in one face `F_R`.

The support depths of successive run vertices increase strictly by (FR.7). Hence nonadjacent run edges have disjoint open support-depth intervals and cannot cross one another. The run is therefore a simple polygonal path.

Its containing face satisfies

\[
\operatorname{span}_N(F_R)
\ge\operatorname{span}_N(R)
\ge{D-O(\sqrt D)\over M}.
\tag{FR.13}
\]

Because `M=o(D)`, the right side tends to infinity. A bounded quadrilateral unit-contact face has diameter at most two. Thus, for all sufficiently large `D`,

\[
\boxed{
F_R\text{ is a bounded exceptional contact face or the outer contact face.}
}
\tag{FR.14}

---

## 4. Edge count, total slack, and matching inside that same face

Write `R_len=|E(R)|`. For each lower edge define its original excess

\[
\sigma_j=|z_j-z_{j+1}|-1>0.
\]

The two-boundary ledger gives

\[
\sum_{j\in R}\sigma_j\le t_D.
\tag{FR.15}
\]

Also

\[
g_j=N\cdot(z_j-z_{j+1})
\le|z_j-z_{j+1}|=1+\sigma_j.
\]

Summing over the selected run,

\[
\operatorname{span}_N(R)
\le R_{\rm len}+\sum_{j\in R}\sigma_j
\le R_{\rm len}+t_D.
\]

Together with (FR.2), this yields (FR.3).

At least half the run edges satisfy

\[
\sigma_j
\le {2t_D\over R_{\rm len}}
\le
(2h_*+o(1)){M\over D}.
\tag{FR.16}
\]

Even and odd path edges are matchings. Keeping the better parity among these good edges proves (FR.4)--(FR.5).

All of these matched pairs lie in the same original exceptional/outer contact face `F_R`.

---

## 5. Terminal deformation produces an exact monotone unit chain

After a child activates, it and its parent move with the same velocity. Thus at terminal activation time the relative vector of a lower gate is still its event vector `d_j`, and

\[
|d_j|=1.
\]

The selected run therefore becomes an exact unit-contact chain at terminal time.

Moreover

\[
N\cdot d_j\ge0
\]

for every run edge, so this exact unit chain is weakly monotone in the support direction. Its total terminal forward progress is

\[
\sum_{j\in R}N\cdot d_j
=
\operatorname{span}_N(R)
-
\sum_{j\in R}\Delta_j.
\]

Using (FR.9) and (FR.2),

\[
\sum_{j\in R}N\cdot d_j
\ge
{D-O(\sqrt D)\over M}-O(1),
\]

which is (FR.6).

This terminal exact chain is an intermediate finite-repair object; it is not asserted to be a triangle-free global minimizer. The original-source conclusion is the long inactive near-unit path and matching in `F_R`.

---

## 6. Useful scales

For

\[
M=\lfloor\sqrt D\rfloor,
\]

the upper-poor branch forces one exceptional/outer contact face containing a simple fully inactive run with

\[
\operatorname{span}_N(R)\ge(1-o(1))\sqrt D,
\]

and a vertex-disjoint matching of

\[
\left({1\over4}-o(1)\right)\sqrt D
\]

pairs satisfying

\[
|x-y|-1\le(2h_*+o(1))D^{-1/2}.
\]

At the reflection-matched scale

\[
M=\lfloor D^{1/4}\rfloor,
\]

one exceptional/outer contact face contains a simple fully inactive run with

\[
\boxed{
\operatorname{span}_N(R)
\ge D^{3/4}-O(D^{1/4}),
}
\tag{FR.17}

and a matching of

\[
\boxed{
\left({1\over4}-o(1)\right)D^{3/4}
}
\tag{FR.18}

pairs satisfying

\[
\boxed{
|x-y|-1
\le
(0.6694959686742\ldots+o(1))D^{-3/4}.
}
\tag{FR.19}

This is a direct bridge from the two-sided reflection repair to one specific original contact face. The remaining task is to exploit the resulting exceptional/outer-face geometry, rather than treating the near-unit pairs as an unlocalized matching.

**Disposition:** in the upper-poor branch, upgraded the lower-run alternative to one support-deep simple inactive path inside a single original exceptional/outer contact face, with the same bounded total slack and a dense near-unit matching. C-II and Level I remain open.
