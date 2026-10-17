> Generated reading edition · [exact source](../../../docs/reports/target_c_oo_dual_tree_complete_rectangle_2026-10-01.md) · source SHA-256 `ddd010a6f06d49429fc1bf43e4a2edf873788beb5ca964f2dc54ebad5d911048`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-98707198A849","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- dense outer-train crossings force a global complete rectangle

Date: 2026-10-01
Base main: b155953053bf2ef081382f57dadf7535615f0e8f
Status: proof-only; C-II remains open.

## 1. Result

Work with two subfamilies $A,B$ of the two fixed Section-90 phase shores after
passing to complete global outer-to-outer stopped trains. Assume

$$
|A|,|B|\le CD
$$

for one fixed $C>0$, and suppose a certified set of actual cross-shore strict-rhombus
crossings has size at least

$$
E\ge \xi D^2
$$

for one fixed $\xi>0$.

Then for all sufficiently large $D$ there are subfamilies

$$
A_0\subseteq A,\qquad B_0\subseteq B
$$

such that every train in $A_0$ crosses every train in $B_0$ in one actual strict
rhombus and

$$
\boxed{
|A_0|\ge \frac{\xi^2}{2C^3}D-1,\qquad
|B_0|\ge \frac{\xi^2}{2C^3}D.
}
\tag{1}
$$

Moreover $A_0$ is one consecutive block on a simple complement-dual path of the
$A$-train crosscuts.

This is stronger than a generic dense-graph biclique statement because it uses the
outer-to-outer crosscut topology. No Fox--Pach theorem, Ramsey argument, or computation
is used.

At the exact rooted endpoint, audited Section 156 gives

$$
L_{OO}\le h,
$$

while current main gives

$$
h=\pi D+o(D).
$$

Hence one may take $C=\pi+o(1)$ in the preceding argument. Therefore any
outer-to-outer crossing subgraph with

$$
E\ge \xi D^2
$$

contains a complete global outer-to-outer rectangle with

$$
\boxed{
|A_0|,|B_0|
\ge
\left(\frac{\xi^2}{2\pi^3}-o(1)\right)D.
}
\tag{2}
$$

Every train in this rectangle is subject to the audited Section-157 two-sided
actual-diameter bracing theorem.

## 2. Same-shore trains are globally noncrossing

All trains on one Section-90 shore have one common phase label, and all their reduced
phases lie in one interval of width

$$
W_D=\frac{4K}{D}.
$$

For large $D$, $W_D<\pi/3$. Thus two trains from the same shore have projective
direction distance strictly less than $\pi/3$.

A strict unit rhombus crossing has projective direction separation at least
$\pi/3$, with strict inequality in the strict-rhombus case. Therefore two complete
trains from the same Section-90 shore cannot cross anywhere in the global strict-
rhombus complex.

Every train considered below has at least one certified crossing, so it is not a
singleton train. Its outer-to-outer midpoint curve is therefore a proper crosscut.
As in the audited dual-tree correction, repeated outer-face vertices may be resolved in
a small regular neighborhood without changing which train pairs cross.

Consequently each of $A$ and $B$ is a family of pairwise noncrossing proper
crosscuts.

## 3. Complement-dual path representation

Remove the $A$-crosscuts from the outer-face disk. Their complement dual $T_A$ is a
tree with one edge for each member of $A$.

For $b\in B$, let $P_b$ be the set of $A$-edges crossed by $b$. Traversing
$b$ moves through complement regions and crosses the corresponding dual edge each
time it meets an $A$-train. Two complete trains cross at most once, so no dual edge
is repeated. A trail without a repeated edge in a tree is a simple path. Hence

$$
\boxed{P_b\text{ is the edge set of one simple path in }T_A.}
\tag{3}
$$

If $P,P'$ are two simple paths in a tree, then $P\cap P'$ is connected or empty.
Thus, after choosing one backbone path $P$, every $P_b\cap P$ is a consecutive
interval in the edge order of $P$.

## 4. A weighted backbone carries quadratic incidence

Let $G=(A,B,E_G)$ be the certified crossing graph with

$$
|E_G|=E\ge \xi D^2,
$$

and let

$$
d_a:=\deg_G(a).
$$

The full path $P_b$ can contain certified and additional actual crossings. Therefore

$$
\sum_{b\in B}\sum_{a\in P_b} d_a
\ge
\sum_{ab\in E_G}d_a
=
\sum_{a\in A}d_a^2.
\tag{4}
$$

By Cauchy--Schwarz,

$$
\sum_{a\in A}d_a^2
\ge
\frac{E^2}{|A|}.
\tag{5}
$$

Averaging (4)--(5) over $b\in B$ gives one $b_*\in B$ such that, for the
backbone path

$$
P:=P_{b_*},
$$

$$
\sum_{a\in P}d_a
\ge
\frac{E^2}{|A||B|}
\ge
\frac{\xi^2}{C^2}D^2.
\tag{6}
$$

Put

$$
\zeta:=\frac{\xi^2}{C^2}.
$$

For every $b\in B$, let

$$
I_b:=P_b\cap P.
$$

These are intervals on $P$. Counting actual crossings along $P$,

$$
\sum_{b\in B}|I_b|
=
\sum_{a\in P}\deg_{\rm actual}(a)
\ge
\sum_{a\in P}d_a
\ge
\zeta D^2.
\tag{7}
$$

No assertion is made that every crossing in (7) belonged to the original certified
edge set. That is unnecessary: every such pair is still an actual crossing of the
same two complete Section-90 trains.

## 5. Consecutive-block double count

Set

$$
\gamma:=\frac{\zeta}{2C}
=\frac{\xi^2}{2C^3},
\qquad
L:=\lfloor\gamma D\rfloor.
\tag{8}
$$

Equation (6) and $\deg_{\rm actual}(a)\le |B|\le CD$ imply

$$
|P|\ge \frac{\zeta}{C}D=2\gamma D,
$$

so $L$-edge blocks exist for all sufficiently large $D$.

If an interval $I_b$ has $s_b$ edges, the number $N_b$ of consecutive
$L$-edge blocks of $P$ contained in $I_b$ is

$$
N_b=\max(0,s_b-L+1)\ge s_b-L+1.
$$

Summing and using (7),

$$
\begin{aligned}
\sum_{b\in B}N_b
&\ge
\sum_{b\in B}|I_b|-|B|(L-1)\\
&\ge
\zeta D^2-CD\cdot\gamma D\\
&\ge
\frac{\zeta}{2}D^2.
\end{aligned}
\tag{9}
$$

The path $P$ has at most $|A|\le CD$ distinct $L$-edge blocks. Hence some
one block $A_0$ is contained in at least

$$
\frac{\zeta D^2/2}{CD}
=
\gamma D
$$

of the intervals $I_b$. Let $B_0$ be those trains. Then

$$
|A_0|=L\ge\gamma D-1,\qquad |B_0|\ge\gamma D,
$$

and every $b\in B_0$ crosses every $a\in A_0$. This proves (1).

## 6. The rectangle is automatically ordered and inverse-phase collapsed

Choose the Section-90 phase labels so that the $B$-label is one step above the
$A$-label. If $a\in A_0$ and $b\in B_0$ cross, the strict-rhombus phase law gives

$$
x_b-x_a=\delta_{ab}>0.
\tag{10}
$$

Because the rectangle is complete, (10) holds for every cross-pair. Therefore

$$
\boxed{
\max_{a\in A_0}x_a
<
\min_{b\in B_0}x_b.
}
\tag{11}
$$

Also all reduced phases remain in the original Section-90 bin, so

$$
0<\delta_{ab}\le \frac{4K}{D}.
\tag{12}
$$

Thus the canonical Section-76 common-cone argument applies to the whole rectangle:
the two shores have one common crossing sign and common crossing order. Its global
diameter estimate gives

$$
D
\ge
\frac{\sqrt3}{2}\bigl(|A_0|+|B_0|\bigr)
-
\frac{\sum_{a,b}\delta_{ab}}{\min(|A_0|,|B_0|)}
-2.
\tag{13}
$$

The defect term is $O_{K,C}(1)$, since

$$
\frac{\sum_{a,b}\delta_{ab}}{\min(|A_0|,|B_0|)}
\le
\frac{4K}{D}\max(|A_0|,|B_0|)
\le 4KC.
\tag{14}
$$

This does not by itself contradict the diameter bound because the coefficient in (1)
can be small. Its use is structural: the quadratic outer-to-outer branch now contains
one explicit global ordered complete rectangle, not merely a dense crossing graph.

## 7. Endpoint O-O branch refinement

Current main takes $\xi=\kappa^2/2$ in the endpoint O-O/interface trichotomy.
If the O-O alternative occurs, (2) gives a complete global O-O rectangle
$A_0\times B_0$ with

$$
\boxed{
|A_0|,|B_0|
\ge
\left(\frac{\kappa^4}{8\pi^3}-o(1)\right)D.
}
\tag{15}
$$

Put

$$
g:=\frac{\kappa^4}{8\pi^3}.
$$

The current narrow-bin star theorem says that all single-star two-sided braces on one
phase shore use at most

$$
C_K=\lfloor4K\rfloor+2
$$

diameter vertices.

Apply this only after extracting the complete rectangle.

Either one shore of the rectangle contains at least

$$
\boxed{
\left(\frac g2-o(1)\right)D
=
\left(\frac{\kappa^4}{16\pi^3}-o(1)\right)D
}
\tag{16}
$$

genuinely split-star trains, or each shore contains at least
$(g/2-o(1))D$ single-star trains. In the latter case, pigeonhole the bracing stars
on each shore. There are fixed diameter vertices $v,w$ and subfamilies
$A_v\subseteq A_0$, $B_w\subseteq B_0$ such that

$$
\boxed{
|A_v|,|B_w|
\ge
\left(\frac{g}{2C_K}-o(1)\right)D
=
\left(\frac{\kappa^4}{16\pi^3C_K}-o(1)\right)D,
}
\tag{17}
$$

every member of $A_v$ is single-star braced by $v$, every member of $B_w$ is
single-star braced by $w$, and every cross-pair in $A_v\times B_w$ is an actual
strict-rhombus crossing. The crossing-direction theorem forces

$$
v\ne w.
\tag{18}
$$

Thus the O-O half of the current endpoint trichotomy can be sharpened to:

1. a linear split-star population lying on one shore of a global ordered complete
   inverse-phase O-O rectangle; or
2. two fixed distinct diameter stars bracing the two shores of a linear-by-linear
   global ordered complete inverse-phase O-O rectangle.

The third current-main alternative, a linear phase-coherent population of endpoints on
global inactive faces, is unchanged.

## 8. Remaining target

The fixed-star O-O branch no longer requires a generic subquadratic crossing-capacity
theorem. Its live object is more rigid:

$$
\boxed{
\text{fixed }v\ne w
+
\text{linear complete O-O rectangle}
+
\text{two-sided Section-157 bracing}
+
\text{inverse-}D\text{ phase collapse}.
}
$$

A closing theorem can now work directly with the common grid order and the two fixed
diameter stars.

The split branch is also more structured than before: a linear split-star family is
one shore of a complete O-O grid and every train crosses the same linear transverse
family. The missing statement is a multiplicity/order obstruction for the two
Section-157 witness stars along that common grid.

The global inactive-interface branch from current main remains separate.

No computation, numerical experiment, verifier, CI result, or unexecuted code is used.
