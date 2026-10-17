> Generated reading edition · [exact source](../../../docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md) · source SHA-256 `43c490a092d644dd42831ec60359701c9c77106f927623c5fd7f0585ba83c83c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2730FC62EBF8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — phase cuts and coherent crossing families

**Date:** 2026-09-05

**Repository state:** `main`, starting commit `89c174120371b8a5482be66282e79f208d8e233f`

**Run type:** complete-solution attempt; closing proofs and audit

**Target:** Level I, selecting Target B

**Active prompt:** Target B uses its [route map](../targets/target-b/README.md) directly

**External web search:** used for a near-miss literature check; no theorem was
imported into the proof. The checked source is Fox--Pach,
[*String graphs and incomparability graphs*](https://math.nyu.edu/~pach/publications/stringpartial071709.pdf).

**Computation:** proof audit and documentation checks; see Section 9

Initial unrelated changes, preserved: modified `docs/prompts/README.md` and
untracked `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`.

## LEVEL I STATUS

**STILL OPEN.** No proof or disproof of the global quantifiers was obtained.

The strongest new result is **NE**: a uniform exclusion of coherent,
core-sized, near-extremal three-class train graphs in the jammed pure-disk
branch. Its proof removes both the earlier additive-block requirement and
the exact-equality requirement. **PC** independently improves the full phase
feedback deletion to boundary order. The general shell inequality and
whole-problem branch coverage are not proved.

## 1. Starting endpoint and proof obligations

The live Target B module, Sections 25 and 36, improves the launch prompt's
threshold to
```math
\mathscr O(A)\ge c_0P,\qquad c_0=\sqrt3/4.
```
For a rhombic complex with outside count $`t`$ and Euler characteristic $`\chi`$,
the equivalent sufficient shell bound is
```math
G+E\ge c_0B+a_0(t+\chi-1),\qquad a_0=\sqrt3/2.
```
A global minimizer satisfies the strict reverse inequality. This is the exact
quantity to change; an uncontrolled boundary-order error is inadmissible.

Target A still requires its source-specific Schur response inequality. Target C
still requires both the shear and fully visible gates. Target B was selected for
its direct packing contradiction and its later concrete phase-star subfrontier.
Only the Target B route was fully bootstrapped; no Target A/C theorem is imported.

Two proposed implications were pursued:

```text
phase-circle cut -> O(D) deleted crossings with an exact real phase potential
 -> diameter-compatible defect contraction [NOT PROVED]
 -> finite strict competitor [NOT PROVED] -> jammed-branch contradiction.

coherent crossing biclique -> D >= (sqrt(3)/2-o(1))(a+b)
 -> exclude a core-sized phase star by the strict global n-1 bound
 -> pure phase-star endpoint excluded
 -> interval extraction + tripartite stability -> NE near-extremal endpoint excluded
 -> general core coverage remains open.
```

Dependencies are the [local structure module](../theory/01-local-structure.md),
Theorems 10.6 and 10.2/Corollary 10.4; the
[Target B module](../targets/target-b/01-jammed-rhombic-branch.md), Sections
36, 49–56; and the [nonlinear regression module](../theory/02-nonlinear-and-regressions.md)
for the scope of global versus local optimality. No train realization across
holes is assumed.

## 2. New proofs

### PC — a boundary-order phase cut (proved)

Let $`\Gamma`$ be the train-crossing graph of any finite strict unit-rhombus
complex satisfying Theorem 10.6. Let $`\phi_v\in\mathbb R/\pi\mathbb Z`$
be its projective directions. A crossing edge has acute angle
$`\pi/3+\delta_e`$, with $`0<\delta_e\le\pi/6`$.
Write $`\Delta=\sum_e\delta_e`$ and
$`E=\sum_e[\sin(\pi/3+\delta_e)-a_0]`$.

There is a set of edges $`F`$ such that
```math
|F|\le\left\lfloor\frac{3\Delta}{\pi}\right\rfloor
\le\lfloor(2+\sqrt3)E\rfloor,
\tag{PC1}
```
and on $`\Gamma-F`$ there are a real potential $`x_v`$ in one interval of
length $`\pi/3`$, and labels $`\ell_v\in\mathbb Z/3`$, satisfying
```math
x_v-x_u=\delta_e>0,\qquad \ell_v-\ell_u=1\pmod3
\tag{PC2}
```
for every edge oriented so that
$`\phi_v-\phi_u\equiv\pi/3+\delta_e\pmod\pi`$.
Choose either orientation at a right-angle crossing and retain that choice.
In particular this orientation of $`\Gamma-F`$ is acyclic and its gain is exact.

**Proof.** Put $`L=\pi/3`$ and reduce every direction modulo $`L`$, obtaining
$`\theta_v\in\mathbb R/L\mathbb Z`$. For each oriented edge $`u\to v`$,
mark the positively oriented arc of length $`\delta_e`$ from $`\theta_u`$
to $`\theta_v`$. For a cut point $`s`$ avoiding the finitely many endpoints,
let $`F_s`$ consist of the edges whose marked arc contains $`s`$. Integration
over the circle gives
```math
\frac1L\int_0^L |F_s|\,ds=\frac{\Delta}{L}.
```
The integer-valued function is constant on each complementary open interval.
At least one such interval has value at most $`\lfloor\Delta/L\rfloor`$.
Choose its cut and lift every $`\theta_v`$ to $`x_v\in(s,s+L)`$.
An uncut marked arc has $`x_v-x_u=\delta_e`$; a cut arc instead has
$`x_v-x_u=\delta_e-L`$. Since
$`\phi_v-x_v\in L\mathbb Z\pmod\pi`$, define $`\ell_v`$ by
$`\phi_v\equiv x_v+L\ell_v\pmod\pi`$. Subtraction along any retained
edge gives its label increment 1. A directed cycle would strictly increase
the real potential back to its starting value, which is impossible.

Finally, the sine chord estimate is
```math
\sin(\pi/3+\delta)-a_0\ge\frac{6(1-a_0)}\pi\delta.
```
Thus $`3\Delta/\pi\le E/[2(1-a_0)]=(2+\sqrt3)E`$, proving PC1. ∎

The weighted version is also exact: for any prescribed weights $`w_e\ge0`$,
some cut satisfies
```math
\sum_{e\in F_s}w_e\le\frac3\pi\sum_e w_e\delta_e.
\tag{PC3}
```
This follows from the same integral. It does **not** assert simultaneous
minimization of several different weighted objectives.

For a jammed survivor, $`\Delta=O(D)`$. Thus PC deletes only $`O(D)`$
crossings from the full graph, rather than the $`o(D^2)`$ pruning of Section 50.
It proves the geometric feedback-set statement left open in Section 49. It
does not delete source points, remove physical rhombi, or preserve a pinned
rank after any physical deletion: $`F`$ is a set of omitted crossing relations.

**Dense-core consequence (proved).** Every retained component of Theorem 50.1
is already acyclic, without a further edge deletion, for sufficiently large
$`D`$ with its parameters fixed. Indeed its graph diameter is at most the
constant $`L_0`$ in (50.4), and every edge defect is at most
$`\epsilon_D=D^{-1+\eta}`$. All its phases modulo $`L`$ lie within circular
distance $`L_0\epsilon_D`$ of a root phase. For large $`D`$ they lie in
one arc of width $`2L_0\epsilon_D<L/2`$. A marked edge arc has length at
most $`\epsilon_D<L/2`$; it cannot travel the long way outside that containing
arc, which would require length at least $`L-2L_0\epsilon_D>L/2`$.
Cut outside the arc. No edge is removed, and PC2 gives a strictly increasing
real potential. Thus the long-directed-cycle alternative in Sections 50–51
is absent on these dense low-defect components. Lemma 50.3 applies to every
such component; its diameter obstruction is still Proposition 50.4.

**Global phase-class reduction (proved).** Apply PC to the full train graph
of a pure rhombic disk and let $`F`$ be its cut set. Put
$`T=|V(\Gamma)|`$, let $`T_i`$ be the sizes of the three labels on
$`\Gamma-F`$, and let $`R`$
be the number of rhombi. Since $`|F|=O(D)`$, Theorem 51.1 gives
```math
R-O(D)
\le \max_i T_i(T-T_i).
\tag{PC4}
```
Thus a survivor has an exact quadratic dichotomy. Either there is a phase class
split with a product $`T_i(T-T_i)`$ carrying the full rhombic bulk, or the
crossing count has a fixed quadratic deficit from every such split. In the first
case, interval extraction IS applies whenever the corresponding pair is
asymptotically complete; CR/PS/NE then exclude the coherent core-sized
near-extremal endpoint. In the second case, the remaining obstruction is a
genuine quadratic phase-density deficit, not an unaccounted feedback-set error.
The estimate is a graph statement about crossing relations; it does not itself
produce a diameter-decreasing motion or an Oler surplus.

**PW — phase-window concentration (proved).** Let Gamma' be an oriented
phase graph with a real potential x_v in [0,L), and suppose each retained
edge u -> v satisfies 0 < x_v-x_u <= tau. Partition [0,L) into half-open
intervals of length tau, and let m_k be the number of trains in interval k,
with T = sum m_k. Every retained edge lies inside one window or joins adjacent
windows. Consequently
```math
|E(\Gamma')| \le \frac12\sum_k m_k^2+\sum_k m_km_{k+1}
\le \frac32 m_*T,\qquad m_*:=\max_k m_k.\tag{PW1}
```
Thus retained edge density |E(Gamma')| >= rho T^2 forces
```math
m_*\ge \frac{2\rho}{3}T.\tag{PW2}
```

**Proof.** Within one window, the oriented crossing graph has at most
binom(m_k,2) edges. Between adjacent windows it has at most m_k m_{k+1}
edges. Summing and using sum m_k^2 <= m_* T and sum m_k m_{k+1} <= m_* T
proves PW1. PW2 follows immediately.

For a jammed pure-disk survivor, take a phase-window length `tau=K/D` after
omitting all crossings with defect greater than `K/D`. The angular-defect
budget gives at most `(D/K) sum_e delta_e = O(D^2/K)` such crossings. Hence,
for fixed large `K`, the remaining quadratic crossing mass forces a phase
window containing `Omega_K(D)` trains. PW is only a concentration statement: it does not
force the window pair to be complete, and it does not supply the diameter
motion or Oler surplus needed for closure.

**SI — sliding-interval obstruction (exact regression).** For integers
$`N\ge k\ge2`$, take two ordered noncrossing families
$`A_1,\ldots,A_N`$ and $`B_1,\ldots,B_N`$, and declare
$`B_j`$ to cross exactly
$`A_j,A_{j+1},\ldots,A_{j+k-1}`$ whenever these indices lie in
$`\{1,\ldots,N\}`$. This is an interval-neighborhood crossing model: each
$`B_j`$ sees one contiguous interval, as forced by the disk cut argument.
It has
```math
E=kN-\frac{k(k-1)}2
\tag{SI1}
```
crossings. Every complete crossing subfamily of sizes $`a,b`$ satisfies
```math
ab\le \left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
\tag{SI2}
```
Indeed, (b) selected intervals have common intersection of size at most
$`k-b+1`$, so $`a\le k-b+1`$, and the product is maximized at the midpoint.
For $`k=\lfloor\rho N\rfloor`$, the graph has quadratic density
$`E/N^2=\rho-\rho^2/2+o(1)), while its largest biclique has product at most
\(\rho^2N^2/4+o(N^2)`$. Thus interval order plus quadratic density alone
does not yield a biclique with product comparable to the total crossing mass.

The model is an exact combinatorial regression, not a geometric packing
certificate: it omits endpoint closure, unit lengths, hull diameter, and KKT
equilibrium. Its role is to reject any proposed coverage proof that uses only
proper-arc interval neighborhoods and edge density. A successful theorem must
use the metric endpoint geometry or the Oler/pocket surplus in addition to SI.

**Literature near-miss.** Fox and Pach, *String graphs and incomparability
graphs*, Theorem 1.1 and Corollary 1.2, prove that for every fixed edge density
$`\varepsilon>0`$, a string graph on $`T`$ curves with at least
$`\varepsilon T^2`$ edges contains a balanced complete bipartite subgraph
with both parts of size $`\delta(\varepsilon)T/\log T`$; the paper states that
the logarithmic dependence is tight up to constants. Train crossing graphs are
string graphs (indeed, in the present route each pair crosses at most once), so
this theorem applies to a dense phase window. It is quantitatively insufficient
for CR: with $`T=O(D)`$, it yields only $`D\ge cD/\log D`$, while a global
diameter contradiction needs a lower bound proportional to $`D`$. The result
also gives no information about the source point set, active diameter pairs, or
Oler surplus. It is therefore recorded as a literature import with a precise
mismatch, not as a bridge theorem.

A separate current-status search found a [2026 announcement](https://web.cs.dartmouth.edu/news/2026/04/student-ideates-ai-longstanding-math-problem)
of a verified AI-assisted solution of Erdős Problem #659, concerning distinct distances. It
is unrelated to Problem #99 and supplies no packing or diameter-minimizer
theorem; this note prevents conflating the two problem numbers.

Swanepoel's [triangle-free minimum-distance paper](https://personal.lse.ac.uk/swanepoe/swanepoel-min-dist.pdf)
also remains a near-miss: it asks whether the sharp contact-edge count is
$`\lfloor2n-2\sqrt n\rfloor`$, without proving it, and gives no
diameter-minimizer consequence. Its conjectural edge constant is therefore not
available for the present problem.

The maintained public entry for [Erdős Problem #99](https://www.erdosproblems.com/99)
still labels the displayed statement open; no newer matching theorem was found in
this targeted search.

### Eppstein boundary-scale barrier (proved consequence)

Eppstein's [Theorem 4.1](https://arxiv.org/abs/1708.05152) for $`n`$-vertex
triangle-free penny graphs is sharp at exactly the scale
needed here, but has no spare constant. In a connected pure rhombic disk with
$`R`$ faces and $`B`$ rhombic boundary edges, Euler gives
```math
e=n+R-1,\qquad B=2(n-R-1).
```
Hence Eppstein's bound
```math
e\le 2n-\tfrac12\sqrt{2\pi\sqrt3\,n}+O(1)
```
implies
```math
B\ge \sqrt{2\pi\sqrt3\,n}-O(1).
```
Combining this with the strict lattice comparison
$`D^2<c(n-1)`$, $`c=2\sqrt3/\pi`$, yields
```math
B\ge \pi D-O(1).
```
On the other hand, the convex-hull perimeter satisfies $`P\le\pi D`$, but a
nonconvex rhombic boundary may have $`B>P`$. Thus the graph theorem only pins
the boundary to the sharp perimeter scale; it cannot by itself produce the
strict linear surplus $`G+E\ge(\sqrt3/4)B`$. A new argument must supply a
positive second-order margin or a certified geometric motion.

### Adversarial audit of the phase-to-shell bridge (completed)

The remaining proposed implication was:

```text
quadratic phase mass in a short window
 -> boundary-order control of G+E
 -> Oler surplus >= (sqrt(3)/4)B.
```

This implication is **rejected as unsupported**. The phase data control only
crossing relations between straight trains. They do not determine which train
endpoints lie on the outer boundary, the number of boundary edges created by
holes or multiple components, or the support function of the geometric union
in the diameter directions. Each of these enters $`G`$ and the topology
correction in the exact shell inequality.

The standard isodiametric inequality gives only

```math
  a_0R+E=|U|\le \pi D^2/4,
```

with no term proportional to the lattice boundary count $`B`$. Quantitative
isodiametric stability likewise measures distance from a disk; it does not
bound $`B`$ for a nonconvex rhombic complex with holes. A boundary made from
many short direction changes can have $`B=\Theta(D)`$ while its convex-hull
area deficit is $`o(D)`$. Therefore a generic area/diameter stability theorem
does not prove the required coefficient $`c_0=\sqrt3/4`$. A valid bridge must
use train endpoints and topology, or construct a strict diameter-decreasing
competitor.

The audit also checks the three common shortcuts. PC does not preserve a
physical rhombus complex after deleting crossing edges; PW does not force a
complete phase pair; and a Fox--Pach biclique is only
$`\Theta(D/\log D)`$ per side. None supplies an omitted hypothesis needed by
the shell theorem. The exact surviving obligation is a **phase-density
transport theorem**: from the PC4 quadratic alternative, derive either the
topology-correct shell surplus or a source-preserving strict competitor, with
all boundary and outside-point terms retained.

### Edge-aligned hole estimate (proved, topology-limited)

There is nevertheless an exact part of the topology correction that can be
closed. Let $`H`$ be a connected complementary hole whose boundary follows
rhombus edges, and suppose $`H`$ is tiled by $`r_H`$ unit rhombi. If $`b_H`$ is
its edge boundary count, then

```math
4r_H=2e_H^{\rm int}+b_H,
\qquad e_H^{\rm int}\ge r_H-1,
```

because the dual adjacency graph is connected. Hence

```math
r_H\ge\frac{b_H-2}{2},qquad
\operatorname{area}(H)\ge a_0r_H
\ge \frac{\sqrt3}{4}(b_H-2).
\tag{HA1}
```

For $`h`$ disjoint edge-aligned holes, summing (HA1) gives

```math
G_{\rm holes}\ge \frac{\sqrt3}{4}B_{\rm holes}
 -\frac{\sqrt3}{2}h.
\tag{HA2}
```

Since $`\chi=1-h`$ for a connected complex with $`h`$ holes, the constant term
in (HA2) is exactly $`a_0(\chi-1)`$. Thus edge-aligned holes cannot create an
unaccounted boundary-order loss: their missing area already pays the topology
correction in the target shell inequality.

The scope is essential. This does not cover non-rhombic exceptional faces,
disconnected components, source points outside the complex, or the outer
boundary (B_{\rm out}). Those cases still require the general topology
transport theorem. The estimate is a proved sublemma, not a Level I closure.

### Reflex-terminal charging regression

The tempting local lemma

```text
linear many degree-three reflex boundary vertices -> E >= c B
```

is false without a global diameter hypothesis. Take an $`m\times m`$ patch of
congruent unit rhombi with acute angle

```math
\theta_m=\pi/3+m^{-3}.
```

It has $`R=m^2`$ cells, $`B=4m+O(1)`$ boundary edges, and $`O(m)`$ boundary
train terminals after the usual train decomposition. (Adding a periodic
one-cell serration gives the same scales with linearly many reflex terminals.)
But

```math
E=m^2\bigl(\sin\theta_m-\sqrt3/2\bigr)=O(m^{-1})=o(B).
```

The patch is only a local geometric regression (it is not asserted to be a
global minimizer); its convex-hull deficit $`G=\Theta(m^2)`$ is precisely what
prevents it from violating the shell inequality. Thus reflex-terminal counts
cannot be converted directly into angular surplus. Any closing theorem must
prove that the same configuration with $`G+E<c_0B`$ is impossible, using the
diameter support geometry or a certified motion.

### CR — coherent bicliques have large diameter (proved for a pure disk)

Let a finite edge-to-edge strict unit-rhombus complex have cell union a
topological disk. Let its vertex set have diameter $`D`$. Suppose it has two
disjoint train families $`\mathcal A,\mathcal B`$, of sizes $`a,b\ge1`$,
such that every member of $`\mathcal A`$ crosses every member of
$`\mathcal B`$. Choose oriented unit train vectors $`u_i,v_j`$, with real
arguments $`\alpha_i,\beta_j`$, so that the directions in either family lie
in an interval of length less than $`\pi/3`$, and
```math
\pi/3<\beta_j-\alpha_i<2\pi/3\quad\hbox{for every }i,j.
\tag{CR1}
```
Put $`\alpha_+=\max_i\alpha_i`$, $`\beta_-=\min_j\beta_j`$, and let
$`e`$ be the unit vector with argument
$`\psi=(\alpha_++\beta_-)/2`$. Then
```math
\boxed{D\ge e\cdot\left(\sum_i u_i+\sum_j v_j\right)-2.}
\tag{CR2}
```
In particular, if after a rotation
$`|\alpha_i|\le\varepsilon`$ and
$`|\beta_j-\pi/3|\le\varepsilon`$, with $`\varepsilon<\pi/12`$, then
```math
\boxed{D\ge(a+b)\cos(\pi/6+2\varepsilon)-2.}
\tag{CR3}
```
The same near-triangular conclusion holds for reference separation $`2\pi/3`$
by reversing vector orientations and interchanging the families.

**Proof of the common order.** Each train centerline is a simple proper arc
of the disk, and any two trains cross at most once (Theorem 10.6).
Members of the same family cannot cross: their projective angular separation
is less than $`\pi/3`$. Cut the disk along the disjoint $`\mathcal A`$ arcs.
The regions and the separating arcs form a tree: inserting each disjoint proper
arc splits one region in two. Every $`\mathcal B`$ arc crosses every tree edge
once. Its region walk therefore traverses all tree edges without repeating an
edge. Such a walk in a tree is a simple path; consequently the entire tree is
a path. All $`\mathcal B`$ arcs meet $`\mathcal A`$ in the same order or
its reverse. The analogous assertion holds with the families interchanged.

Orient the $`u_i`$-centerlines so their elementary displacement directions
are in $`(\alpha_i+\pi/3,\alpha_i+2\pi/3)`$, and the
$`v_j`$-centerlines in the reverse transverse orientation, so their
displacement directions are in
$`(\beta_j-2\pi/3,\beta_j-\pi/3)`$. At their crossing rhombus, these
displacements are respectively $`v_j`$ and $`u_i`$. The crossing sign is
therefore the same for every pair. Relative to each oriented $`\mathcal A`$
arc, every oriented $`\mathcal B`$ arc traverses its two sides in the same
order, so reversal of the common order cannot occur. Label the families so
every oriented $`\mathcal A`$ arc meets $`B_1,\ldots,B_b`$ and every
oriented $`\mathcal B`$ arc meets $`A_1,\ldots,A_a`$.

**Proof of the projection estimate.** Follow $`A_1`$ from the center of its
crossing with $`B_1`$ to the center of its crossing with $`B_b`$, then
follow $`B_b`$ to the center of its crossing with $`A_a`$. Both endpoints
belong to the convex hull of the original vertices, so their distance is at
most $`D`$.

Every elementary displacement of the first leg has angle in
$`(\alpha_1+\pi/3,\alpha_1+2\pi/3)`$; every displacement of the second
leg has angle in $`(\beta_b-2\pi/3,\beta_b-\pi/3)`$. Condition CR1 implies
```math
\alpha_i+\pi/6<\psi<\alpha_i+5\pi/6,
\qquad
\beta_j-5\pi/6<\psi<\beta_j-\pi/6
```
for all $`i,j`$. For example, the stronger upper restriction
$`\psi<\beta_- -\pi/6`$ follows from
$`\beta_- -\alpha_+>\pi/3`$, and
$`\beta_-<\min_i\alpha_i+2\pi/3`$ supplies the other upper bound;
the lower bounds are analogous. Thus both displacement cones have nonnegative
projection onto $`e`$.

The selected crossing rhombi on the first leg contribute
$`v_1/2+v_2+\cdots+v_{b-1}+v_b/2`$, and on the second leg contribute
$`u_1/2+u_2+\cdots+u_{a-1}+u_a/2`$. If a family has size one, its leg
is empty and its contribution is zero. All intervening rhombi contribute
nonnegative projection. Relative to $`\sum_i u_i+\sum_jv_j`$, the endpoint
half-vectors lose at most 2 in projection, including the size-one cases.
Projection of the endpoint displacement proves CR2.

Under the near-triangular assumptions, $`|\psi-\pi/6|\le\varepsilon`$.
Every selected unit vector therefore projects at least
$`\cos(\pi/6+2\varepsilon)`$ onto $`e`$. This proves CR3. ∎

No additive block or identification of train-coordinate bases appears in this
argument. Intervening trains are allowed without a bound on their number.
The proper-crosscut argument is why the disk hypothesis is retained.

### PS — phase-star exclusion without additive blocks (proved)

There is no sequence of triangle-free pure-rhombic-disk global minimizers
with $`M\to\infty`$, three phase classes of sizes
$`0\le a\le b\le M`$, $`b\ge1`$,
```math
R=M(a+b)+o(M^2),
\tag{PS1}
```
and a complete crossing family between the $`M`$ class and the $`b`$ class,
whose directions lie within $`o(1)`$ of two triangular directions. The three
classes exhaust the trains, as in Section 56.

**Proof.** CR gives
```math
D^2\ge(3/4-o(1))(M+b)^2.
```
For a pure disk, $`n=R+T+1`$, where $`T=M+a+b=O(M)`$. With
$`c=2\sqrt3/\pi`$, the strict global comparison gives
```math
D^2<c(n-1)\le2cMb+o(M^2).
```
Writing $`t=b/M\in(0,1]`$, the difference of the leading coefficients is
```math
\frac34(1+t)^2-2ct
=\frac34(1-t)^2+(3-2c)t>0.
```
This is uniformly positive even on $`[0,1]`$: for $`t\le1/2`$ the first
term is at least $`3/16`$, and for $`t\ge1/2`$ the second is at least
$`(3-2c)/2>0`$, since $`c<3/2`$. The errors tend to zero and cannot close
this fixed gap. Thus no lower bound on $`b/M`$ is needed. ∎

In particular the exact balanced Section 52 phase endpoint is excluded when
it accounts for the quadratic core: its equality rule supplies a complete
$`m\times m`$ pair, $`R=2m^2+o(m^2)`$, and $`n=2m^2+o(m^2)`$.
CR gives $`D^2\ge(3-o(1))m^2`$, against
$`D^2\le(4\sqrt3/\pi+o(1))m^2`$. The class directions must be coherent;
the combinatorial equality alone is not sufficient.

### IS — extracting a complete family from almost all crossings (proved)

Let $`\mathcal A,\mathcal B`$ be two disjoint train families in a pure disk,
of sizes $`p,q`$, with members of $`\mathcal A`$ internally noncrossing.
Suppose at most $`\epsilon pq`$ of their possible pairs fail to cross,
where $`0\le\epsilon<1`$. There are complete crossing subfamilies of sizes
```math
p'\ge(1-\epsilon)p-2\lceil\sqrt\epsilon\,p\rceil,
\qquad q'\ge(1-\sqrt\epsilon)q,
\tag{IS1}
```
whenever the first bound leaves a nonempty family. For $`\epsilon=0`$, take
the original families.

**Proof.** Some $`B_0`$ crosses a set $`\mathcal A_0`$ of at least
$`(1-\epsilon)p`$ trains. Cut the disk along these disjoint arcs. As in CR,
the region tree is a path because $`B_0`$ traverses each of its edges once.
Any other $`B`$ crosses a contiguous interval of these ordered arcs: its
walk in the region tree cannot repeat an edge, by the two-crossing exclusion,
so its traversed edges form a subpath. At least $`(1-\sqrt\epsilon)q`$
members of $`\mathcal B`$ miss at most $`\sqrt\epsilon\,p`$ members of
the entire $`\mathcal A`$ family, by counting missing pairs. Each such
interval misses at most that many members of $`\mathcal A_0`$. Remove the
first and last $`\lceil\sqrt\epsilon\,p\rceil`$ arcs of $`\mathcal A_0`$.
Every good interval contains the common remainder, proving IS1. ∎

IS is a geometric assertion about actual train crossings. It is false as a
general assertion about dense bipartite graphs; the interval proof is essential.

### TS — stability of the balanced tripartite endpoint (proved)

Let a triangle-free tripartite graph have three classes of size $`m\ge1`$
and at least $`(2-\epsilon)m^2`$ edges. If
$`0<\epsilon\le1/256`$, one pair of classes has at least
```math
(1-3\epsilon^{1/4})m^2
\tag{TS1}
```
edges. At $`\epsilon=0`$, Section 52 with correction EC gives a complete
class pair.

**Proof.** Write $`x_{ab},y_{bc},z_{ca}`$ for edge indicators and
$`d(a,b,c)=2-x_{ab}-y_{bc}-z_{ca}\ge0`$. Their total is at most
$`\epsilon m^3`$. Put $`\eta=\epsilon^{1/4}\le1/4`$.
If the $`A`$-$`B`$ pair misses fewer than $`\eta m^2`$ edges, TS1 already
holds. Otherwise choose a nonedge $`a_0b_0`$ with
```math
\sum_{b,c}d(a_0,b,c)\le\eta m^2,\quad
\sum_{a,c}d(a,b_0,c)\le\eta m^2,\quad
\sum_c d(a_0,b_0,c)\le\eta m.
```
Such a pair exists: violations of the first two conditions exclude at most
$`\eta^3m`$ vertices in each respective class, hence at most
$`2\eta^3m^2`$ pairs. Violations of the third exclude at most
$`\eta^3m^2`$ pairs. Their union has size at most
$`3\eta^3m^2<\eta m^2`$.

Let $`C'`$ consist of common neighbors of $`a_0,b_0`$ in $`C`$. Since
$`a_0b_0`$ is a nonedge, $`|C'|\ge(1-\eta)m`$. Partition $`A`$ as
$`A_1=N_A(b_0)`$ and $`A_0=A\setminus A_1`$, and partition $`B`$
analogously using $`a_0`$. Triangle-freeness implies that every member of
$`A_1`$ or $`B_1`$ has no neighbor in $`C'`$. Thus each triple in
$`A_1\times B_1\times C'`$ has deficit at least one, giving
```math
|A_1||B_1|\le\frac{\epsilon}{1-\eta}m^2.
```
One of $`|A_1|,|B_1|`$ is at most
$`\eta^2m/\sqrt{1-\eta}`$. Suppose it is $`|A_1|`$; the other case is
symmetric. Missing $`A_0`$-$`C'`$ edges are counted exactly by the
deficits $`d(a,b_0,c)`$, whose total is at most $`\eta m^2`$.
Adding pairs incident to $`A_1`$ and those outside $`C'`$, the total
missing $`A`$-$`C`$ pairs is at most
```math
\left(2\eta+\frac{\eta^2}{\sqrt{1-\eta}}\right)m^2
\le3\eta m^2.
```
This is TS1. ∎

### NE — coherent near-extremal three-class cores are excluded (proved)

There is no sequence of triangle-free **jammed pure-rhombic-disk** global
minimizers with a train subgraph $`H`$, three classes of sizes
$`0\le a\le b\le M`$, $`M\to\infty`$, and the following properties:

1. The directions in the three classes lie within $`o(1)`$ of
   $`\phi,\phi+\pi/3,\phi+2\pi/3`$ projectively.
2. $`|E(H)|=M(a+b)-o(M^2)`$.
3. The number of all source rhombi is $`R=M(a+b)+o(M^2)`$.

Here a pure disk has the source as exactly its vertex set, and its full bounded
contact faces are the rhombi forming the disk. The subgraph may omit other
trains and crossings; these assumptions explicitly
require it to account for the quadratic rhombic core. The conclusion does not
assume an additive block or an exact complete crossing family.

**Proof.** The jammed estimates give $`T=O(D)`$, and the pure disk identity
gives $`n=R+T+1`$. Since $`M\le T`$, we have $`M=O(D)`$. Conversely,
```math
D^2<c(R+T)=O(M^2)+O(D)
```
implies $`D=O(M)`$. Consequently $`D=\Theta(M)`$, $`T=O(M)`$, and
```math
D^2\le cM(a+b)+o(M^2).
\tag{NE1}
```
Pass to a subsequence on which $`a/M\to r`$ and $`b/M\to t`$.
The lower bound $`D=\Omega(M)`$ and NE1 force $`t>0`$.

If $`r<1`$, write $`e`$ for the $`M`$-$`b`$ crossing count in $`H`$,
and $`f`$ for the $`M`$-$`a`$ count. The triple-counting proof of Section
51 gives the exact deficit inequality
```math
M(a+b)-|E(H)|\ge
(1-a/M)(Mb-e)+(1-b/M)(Ma-f).
```
The coefficients and missing counts are nonnegative. Hence $`Mb-e=o(M^2)`$.
Since $`b/M\to t`$, this class pair is asymptotically complete. If $`b`$ is
bounded along the subsequence, then $`a+b=o(M)`$, so NE1 gives
$`D^2=o(M^2)`$, contradicting $`D\ge cM`$ from $`M\le T=O(D)`$. We may
therefore assume $`b\to\infty`$. Applying IS to the actual crossing graph
extracts families of sizes $`M-o(M)`$ and $`b-o(b)`$. Members of either
family are internally noncrossing because of phase coherence. CR therefore gives
```math
D^2\ge(3/4-o(1))(M+b)^2.
```
Comparison with NE1 and $`a\le b`$ contradicts the same positive coefficient
gap as PS.

If $`r=1`$, then $`t=1`$. Trim the two larger classes to size
$`m=a=M-o(M)`$. This removes only $`o(M^2)`$ edges, since at most
$`o(M)`$ vertices are removed and each has degree at most $`3M`$ in $`H`$.
The resulting balanced graph has $`2m^2-o(m^2)`$ edges. TS supplies a
class pair with $`(1-o(1))m^2`$ edges; IS gives complete crossing
subfamilies of sizes $`(1-o(1))m`$ each. CR yields
$`D^2\ge(3-o(1))M^2`$, whereas NE1 gives
$`D^2\le(2c+o(1))M^2`$. Since $`2c<3`$, this is impossible.
Every subsequential case has been excluded, proving NE. ∎

The exclusion is uniform: there are $`\eta_0>0`$ and $`M_0<\infty`$ such
that no such jammed pure-disk global minimizer with $`M\ge M_0`$ has all
three phase errors at most $`\eta_0`$,
$`0\le M(a+b)-|E(H)|\le\eta_0M^2`$, and
$`|R-M(a+b)|\le\eta_0M^2`$. Otherwise choosing violations with tolerance
$`1/k`$ and $`M\ge k`$ would contradict the sequential theorem NE.
This is a uniform finite threshold for this subbranch, not for Level I.

NE settles the coherent, core-sized near-equality question left by Sections
51–56. It does not force a general survivor into that near-equality regime.
Several macroscopic grains, or a phase graph with a fixed quadratic deficit
from its class-sensitive bound, remain outside its hypotheses.

### EC — precise correction to Section 52 (regression and repaired statement)

Section 52's wording “complete bipartite graph” is stronger than its proved
adjacency rule. For $`m=2`$, take classes
$`A=\{a_0,a_1\}, B=\{b_1,b_2\}, C=\{c_1,c_2\}`$, and edges all four
$`B`$-$`C`$ pairs, both $`a_0`$-$`C`$ pairs, and both
$`a_1`$-$`B`$ pairs. Every tripartite triple has exactly two edges and
there are eight edges, but the graph is not complete bipartite: its connected
bipartition is $`\{a_0,b_1,b_2\}\sqcup\{a_1,c_1,c_2\}`$ and
$`a_0a_1`$ is absent.

The correct conclusion is the cross-colour adjacency rule stated there,
**restricted to pairs from different original classes**. At most one original
class can split between the two colours, and the other two are monochromatic
with opposite colours. Indeed, if two classes split, choose one member of each
in the colour of any vertex of the third class; that triple would have no edges,
contradicting equality. With no split, the same argument requires both colours
to occur. With one split, the two monochromatic classes must have opposite
colours for the same reason. Consequently a complete $`m\times m`$ pair
always exists. PS uses only this valid consequence.

## 3. Exact advances and surviving obligations

PC changes the full train feedback deletion scale to $`O(D)`$, with exact
constants, and supplies an acyclic real phase potential on the remainder.
CR/PS remove the additive-realization hypothesis from the coherent pure-disk
phase-star exclusion. IS and TS push this through near equality: NE excludes
every coherent three-class core meeting its quantitative coverage and
near-extremality hypotheses, with a uniform positive tolerance. No result
proves that every survivor contains such a core.

The proposed continuation of PC is still conditional. In pure train coordinates,
take $`v_v=-x_v`$. Retained defects have derivative $`-\delta_e`$, while
deleted defects have derivative $`L-\delta_e>0`$. Every unit contact is
preserved by the exact angle path, and every initially strict lower constraint
stays strict for sufficiently small time. Active diameter inequalities have
no proved sign. Even nonpositive first derivatives need the existing
second/higher-order analysis; tangent quartic blocking remains possible.

## 4. Exact remaining lemma

No full shell inequality was proved. A concrete next sufficient subtheorem is:

> **Phase-cut coverage theorem.** In every sufficiently large triangle-free
> jammed pure-disk global minimizer satisfying $`G+E<c_0B`$, either the
> coverage, coherence, and near-extremality hypotheses of NE hold for a
> three-class core, or an actual source-cardinality, unit-separated configuration
> of diameter strictly below $`D`$ can be constructed using the PC phase
> potential and its explicitly retained exceptional crossings.

This theorem must prove its dichotomy; PC alone does not provide it. Even this
pure-disk result would require a topology-correct extension and the flexible
branch before yielding Level I.

## 5. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| PC1–PC3 | proved | Exact phase-circle averaging and lifting |
| CR | proved for a pure disk | Common crossing order plus nonnegative projection cones |
| PS | proved | CR contradicts the strict global diameter comparison |
| IS and TS | proved | Ordered intervals and a quantitative triple-deficit argument |
| NE and its uniform-tolerance consequence | proved | Stability, interval extraction, and the CR/global coefficient gap |
| SI sliding-interval biclique extraction | regression | Dense interval crossing graphs can have only a small biclique |
| Section 52 literal complete-bipartite wording | rejected | Six-vertex equality regression EC |
| Section 52 cross-class colour rule and full phase pair | proved | Existing proof, with explicit split-class audit |
| HA edge-aligned-hole estimate | proved, topology-limited | Dual adjacency count gives the exact Euler correction for rhombic holes |
| Eppstein boundary-scale consequence | proved barrier | Forces $`B\ge\pi D-O(1)`$, with no positive surplus margin |
| Sparse phase deletion implies shell-rank deficiency | conjectural route | Both dimensions are boundary order; no rank transport proved |
| Defect contraction implies diameter contraction | rejected as an inference | Active diameter derivatives are uncontrolled |
| Every survivor has a core satisfying NE | conjectural route | Multiple grains and a fixed phase-density deficit remain |
| Whole-problem solution | not obtained | Flexible and general jammed survivors remain |

## 6. Regression audit

| Regression | Disposition |
| --- | --- |
| Square | CR is a finite lower bound, not a contradiction; the square can block angle contraction through its two diameters |
| Regular shells and prime polygon local minima | No core-sized pure-rhombic star hypothesis; no claim turns their stresses into global certificates |
| Five-sector near-equilateral complexes | Compatible with PC and CR; their pinned boundary is not the diametral hull of a global minimizer |
| Balanced five-direction cyclic crossing graph | Sharp angular PC bound; see Section 7 |
| 11-point sun | CR permits it; PS is asymptotic and requires core-sized counts; canonical strict competitor already excludes it globally |
| Disk-clipped vanishing-shear oblique lattices | Compatible with CR; no core-sized complete star is inferred from their density |
| Quadratic raw support depth | No depth-to-Oler conversion is used; Section 25 cancellation remains binding |
| Tangent quartic blocker | Untouched; PC angle contraction is not a finite diameter certificate |
| Holes, components, outside source vertices | PC is abstract and still applies to the train graph; CR/PS deliberately retain the pure-disk scope |
| Full-rank planar response / Hall overlaps | No Schur nullity or matching transport is asserted |

## 7. Sharpness and failed closing mechanisms

PC's angular coefficient cannot be improved for arbitrary train geometry.
Take five direction classes of size $`s`$, at projective directions
$`0,\pi/5,2\pi/5,3\pi/5,4\pi/5`$, with crossings when directions differ
by $`2\pi/5`$ projectively. The crossing graph is the balanced blow-up of
a five-cycle. Orient each step by $`+2\pi/5`$. Every edge has
$`\delta=\pi/15`$, so $`3\Delta/\pi=s^2`$. There are $`s^5`$
directed five-cycles and each edge lies in $`s^3`$ of them. Every acyclic
edge deletion therefore has size at least $`s^2`$. Deleting all edges of
one class pair attains it. This proves sharpness, not global optimality.

This is geometrically realized by the five-sector construction of local
Theorem 10.10 with all five successive angles $`2\pi/5`$ (its parameter
$`\varepsilon=\pi/15`$ lies outside that theorem's small-parameter range,
so the following direct check is needed). For regular unit directions
$`w_0,\ldots,w_4`$, take
$`\bigcup_i\{aw_i+bw_{i+1}:0\le a,b\le s\}`$.
Adjacent sectors meet along their radial chains; points off that chain on
opposite sides have perpendicular separation at least $`2\sin(2\pi/5)>1`$.
Within a sector, the squared norm of an integer difference with opposite-sign
coefficients is
$`(p-q)^2+2pq(1-\cos(2\pi/5))>1`$ for $`p,q\ge1`$, and same-sign
coefficients give equality only for coordinate unit steps. Nonadjacent cones
are separated by at least $`2\pi/5`$, and their nonzero lattice points
have norm at least one, giving distance strictly greater than one.
Thus the contacts are exactly the sector-grid edges; their faces are strict
rhombi. Each of the five train classes has $`s`$ members and crosses just
its two neighboring classes. The complex is a disk. No extremality is claimed.

Two materially different closing attempts remain unsuccessful:

1. **Variational:** PC supplies a simultaneous contraction of retained defects,
   but deleted defects expand and active diameters can expand. The phase-cut
   count cannot remove their gradient or higher-order certificates.
2. **Geometric:** CR handles intervening trains. IS/TS also solve extraction
   near the coherent class-sensitive density endpoint, giving NE. General
   dense phase graphs can remain a fixed quadratic amount below that endpoint,
   and several grains can share the bulk. Neither the phase-energy estimate
   nor PC rules out those alternatives. Assuming near-extremal one-core
   coverage would simply replace the missing shell theorem.

## 8. Literature

### Fox and Pach, *String graphs and incomparability graphs*

- Link: https://math.nyu.edu/~pach/publications/stringpartial071709.pdf
- Theorem 1.1 and Corollary 1.2.
- Exact conclusion: every string graph with at least $`\varepsilon T^2`$ edges
  contains a balanced biclique with both parts of size
  $`\delta(\varepsilon)T/\log T`$; the logarithmic dependence is stated to be
  tight up to constants.
- Applicability: train crossing graphs are string graphs, with at most one
  crossing per pair in the present rhombic setting.
- Mismatch: $`T=O(D)`$, so the resulting CR lower bound is only
  $`O(D/\log D)`$, not proportional to $`D`$. The theorem does not encode
  unit lengths, source points, active diameters, KKT support, or Oler surplus.
- Disposition: literature import recorded as a quantitative near-miss; it does
  not close the phase-density transport theorem.

All other external baseline statements used are already audited in the repository.
PC, CR, PS, IS, TS, NE, PW, and EC have self-contained proofs above.

## 9. Computation and reproducibility

The exact finite-model script is
[`research/phase_cut_certificate.py`](../../../research/phase_cut_certificate.py).
Run `python3 research/phase_cut_certificate.py`. Arithmetic uses rational
multiples of pi (`fractions.Fraction`) and integer graphs. It checks all cut
intervals in a 30-direction model, including right-angle ties, and returns
135 edges, minimum cut 35, mean cut 75/2. For the five-cycle blow-ups, it
certifies optimum feedback deletion 1 and 4 for sizes one and two, excluding
all 1 and 1351 smaller deletion sets respectively. All 4096 balanced tripartite
graphs with class size two were checked: nine attain eight edges, all obey the
repaired colour rule and contain a complete phase pair. EC is verified.

Encoded assumptions are the projective angle/gain relations and finite graph
conditions. Planar realization, unit-contact distances, stresses, and global
optimality are omitted. A successful run certifies these finite checks only.
Computation is not a premise of the general proofs.

The separate adversarial pass checked:

- PC lifts are modulo $`\pi/3`$, while the class labels are modulo three;
  retained increments are exact, including a chosen right-angle orientation.
- The bound counts removed crossing relations, not physical constraints or points.
- CR uses proper arcs of one disk. Cutting along a disjoint family gives a tree;
  a transverse arc meeting every cut once forces that tree to be a path. Thus
  no unordered-biclique-to-grid identification is hidden in the proof.
- The orientation of each crossing is fixed by CR1, so the two common orders
  are compatible with the two forward path legs.
- All intervening displacement projections are nonnegative. The four endpoint
  half-vectors lose at most 2, independently of the number of intervening trains.
- Cell centers lie in the original convex hull, whose diameter is the source
  diameter; no scaffold or separate optimum is substituted.
- PS uses the original cardinality identity $`n=R+T+1`$. Its coefficient gap
  is uniform for $`0\le b/M\le1`$, including a vanishing smaller class.
- IS uses the actual crossing graph, not an abstract dense bipartite graph;
  its interval property follows from proper arcs and the no-repeat crossing rule.
- TS counts nonnegative triple deficits and explicitly bounds all excluded
  anchor pairs. It imports no graph removal or stability theorem.
- NE retains `T=O(D)` from jamming, derives `D=Theta(M)`, and accounts for
  every source rhombus in its coverage hypothesis. The unbalanced and balanced
  subsequential limits exhaust all possibilities. Its uniform-tolerance
  conclusion follows by a sequence of counterexamples, not an invented rate.
- Excluding this reduced subcase does not exclude all contact-minimal normal
  forms; no global-quantifier claim is made beyond the stated hypotheses.

## 10. Promotion

**Promote now:** PC, PW, CR, PS, IS, TS, NE, HA and the EC correction passed the proof/scope audit.
Their full proofs remain here as an audited addendum, explicitly indexed by the
Target B route map. Section 52's erroneous complete-bipartite wording is corrected
in place; the full-pair conclusion is preserved. Later conditional additive-block
frontier text is marked superseded by CR/PS, with the pure-disk and coverage
limitations retained. Target B has no separate active continuation prompt, so
its route map carries the updated operational endpoint. No Target A/C module or
pre-existing prompt change is altered.

Files changed by this run:

- `docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md` — full proofs,
  regression, audit, and handoff;
- `docs/targets/target-b/README.md` — promotion index and exact surviving endpoint;
- `docs/targets/target-b/01-jammed-rhombic-branch.md` — EC correction and explicit
  supersession notes;
- `research/phase_cut_certificate.py` — exact finite checks;
- `research/README.md` — encoded/omitted assumptions and reproduction command.

Documentation verification: relative links in all four affected Markdown files
resolve (24 links at the check); no numbered section was added outside the route
map, and all promoted labels are indexed there. The route map is the active
Target B continuation context. No PDF or extracted-text copy was added.
Whitespace checks include both tracked changes and the two newly created files.

## 11. Highest-value next theorem

Prove a phase-density transport theorem: in a pure-disk survivor satisfying PC4,
convert its remaining quadratic phase-density deficit into either the shell
surplus $`G+E\ge c_0B`$ or a finite diameter-decreasing motion. The proof must
use the exact (O(D)) exceptional crossing set and certify every active diameter
constraint. A large coherent biclique is one possible route; NE shows that this
route already handles the near-extremal three-class regime.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN
New proofs: O(D) phase feedback deletion with an exact real acyclic potential;
coherent crossing-biclique diameter lower bound without additive-block hypotheses;
near-complete crossing extraction, tripartite stability, and uniform exclusion
of coherent core-sized near-extremal three-class phase graphs (NE); and the
global phase-class reduction PC4; plus the edge-aligned-hole estimate HA matching
the Euler correction.
Exact target still open: Oler surplus >= (sqrt(3)/4) P, topology-correctly;
the flexible branch also remains open.
No-go: phase contraction does not imply diameter contraction; boundary-order
deletion does not imply boundary-order rank deficiency; SI rules out a generic
interval-biclique shortcut; PC4's quadratic phase deficit and NE core coverage
remain unproved routes.
Next theorem: phase-cut coverage (Section 4), then topology and flexible coverage.
Authority: docs/targets/target-b/README.md and its indexed modules/addenda;
shared theory modules. PC/PW/CR/PS/IS/TS/NE/HA and EC are promoted through the Target B map.
```
