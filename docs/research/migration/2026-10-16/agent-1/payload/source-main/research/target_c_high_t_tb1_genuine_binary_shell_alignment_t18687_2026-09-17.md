# Target C-II — genuine binary TB1 blockers align with the common row

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the parity-thinned one-sign strong-TB1 finite-swap reduction; no canonical promotion claimed  
**Scope:** genuinely binary `11`-only obstructions in the retained exact-swap family through `t=(q-k)/D<=1.8687`  
**Dependencies:** max-swap inheritance; common oriented swap-axis cone; uniform exact-swap scale; global boundedness of row-parallel `D-O(D^-2)` pairs  
**Certificate:** `research/verify_target_c_high_t_tb1_genuine_binary_shell_alignment_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding max-swap inheritance theorem forced every genuine two-coordinate obstruction into one of the two ultra-thin shells

\[
1<|xy|\le1+O(D^{-2})
\]

or

\[
D-O(D^{-2})\le|xy|<D.
\]

The shell statement alone did not record the direction of these pairs. The singleton-safety inequalities do: every genuine binary blocker is also asymptotically **parallel to the common train row direction**.

Let `w_*` be the common oriented strong-TB1 swap axis and let `u_*=w_*^\perp` be the common row direction. Then, uniformly over every genuine binary blocker,

\[
\boxed{
\begin{array}{ll}
\text{lower shell:}&
|xy|=1+O(D^{-2}),\quad
|(y-x)\cdot w_*|=O(D^{-1}),\\[1ex]
\text{upper shell:}&
|xy|=D-O(D^{-2}),\quad
|(y-x)\cdot w_*|=O(1).
\end{array}}
\]

In either case

\[
\boxed{
d_{\mathbb{RP}^1}([xy],[u_*])=O(D^{-1}).}
\]

This has two global consequences.

1. The genuine **upper** binary family contains only `O(1)` pairs source-wide, by the existing boundedness theorem for row-parallel `D-O(D^-2)` chords. Thus positive-density two-coordinate coupling cannot hide near the diameter boundary.
2. The genuine **lower** binary family is a disjoint union of monotone paths. Its graph has maximum degree at most two, has no cycle, and along every path the vertices occur in the same order as their `u_*` coordinate. Every edge has length `1+O(D^-2)` and direction within `O(D^-1)` of the common row.

So the only potentially large genuinely binary interaction left in the strong-TB1 finite-swap system is a near-collinear forest of ultra-near-unit pairs.

---

## 1. Exact inequalities for a genuine binary blocker

Use the two-coordinate notation

\[
r_{00}=r,
\qquad
r_{10}=r-q_iw_i,
\qquad
r_{01}=r+q_jw_j,
\qquad
r_{11}=r-q_iw_i+q_jw_j.
\tag{GA.1}
\]

Assume

\[
q_i\ge q_j,
\qquad
s={q_j\over q_i}\in(0,1],
\qquad
t=1-s.
\tag{GA.2}
\]

The strong-TB1 common-axis theorem gives fixed constants `Q,C,C_*` such that

\[
q_i\le {Q\over D},
\qquad
|w_i-w_j|\le {C\over D},
\qquad
|w_i-w_*|,|w_j-w_*|\le {C_*\over D}.
\tag{GA.3}
\]

Put

\[
x=r\cdot w_i,
\qquad
y=r\cdot w_j,
\qquad
\delta=y-x=r\cdot(w_j-w_i).
\tag{GA.4}
\]

A **genuine binary blocker** means that both singleton states are safe but the joint state is bad:

\[
r_{10},r_{01}\text{ satisfy the relevant bound,}
\qquad
r_{11}\text{ violates it.}
\tag{GA.5}
\]

The max-swap inheritance theorem already gives the corresponding `D^-2` shell with a bound retaining the local `q_i` scale. We now combine that bound with (GA.5).

---

## 2. Lower genuine blockers have transverse projection `O(D^-1)`

Assume

\[
|r|>1,
\qquad
|r_{10}|>1,
\qquad
|r_{01}|>1,
\qquad
|r_{11}|\le1.
\tag{GA.6}
\]

Write

\[
A_0=|r|^2-1>0.
\tag{GA.7}
\]

The max-swap inheritance proof gives uniformly

\[
A_0
\le
{2Cq_i\over D}
+{sC^2q_i^2\over D^2}
+tq_i^2.
\tag{GA.8}
\]

Hence

\[
\boxed{{A_0\over q_i}=O(D^{-1}).}
\tag{GA.9}
\]

Singleton safety at `i` gives

\[
A_0-2q_ix+q_i^2>0,
\]

so

\[
\boxed{x<{A_0+q_i^2\over2q_i}=O(D^{-1}).}
\tag{GA.10}
\]

We need the matching lower bound for `x`.

### Case 1: `s>=1/2`

Singleton safety at `j` gives

\[
A_0+2q_jy+q_j^2>0,
\]

hence

\[
y>-{A_0+q_j^2\over2q_j}=O(-D^{-1}).
\tag{GA.11}
\]

More precisely the right side has magnitude `O(D^-1)` because `q_j=sq_i` with `s>=1/2` and (GA.9) holds. Also, since `|r|=1+O(D^-2)`,

\[
|\delta|
\le |r|\,|w_j-w_i|
=O(D^{-1}).
\tag{GA.12}
\]

Thus

\[
x=y-\delta>-O(D^{-1}).
\tag{GA.13}
\]

### Case 2: `s<1/2`

Here `t>1/2`. Joint lower-bound violation gives

\[
A_0-2tq_ix+2sq_i\delta+|q_iw_i-q_jw_j|^2\le0.
\tag{GA.14}
\]

Therefore

\[
x
\ge
{s\over t}\delta
+{A_0+|q_iw_i-q_jw_j|^2\over2tq_i}
\ge
{s\over t}\delta.
\tag{GA.15}
\]

Since `s/t<1` and (GA.12) holds,

\[
x>-O(D^{-1}).
\tag{GA.16}
\]

Together with (GA.10),

\[
\boxed{|r\cdot w_i|=|x|=O(D^{-1}).}
\tag{GA.17}
\]

Using the common-axis estimate in (GA.3),

\[
|r\cdot w_*|
\le |r\cdot w_i|+|r|\,|w_i-w_*|
=O(D^{-1}).
\tag{GA.18}
\]

Since `|r|=1+O(D^-2)`, this is equivalent to

\[
\boxed{
d_{\mathbb{RP}^1}([r],[u_*])=O(D^{-1}).}
\tag{GA.19}
\]

---

## 3. Upper genuine blockers have transverse projection `O(1)`

Assume instead

\[
|r|<D,
\qquad
|r_{10}|<D,
\qquad
|r_{01}|<D,
\qquad
|r_{11}|\ge D.
\tag{GA.20}
\]

Write

\[
B_0=D^2-|r|^2>0.
\tag{GA.21}
\]

The max-swap inheritance proof gives

\[
B_0
\le
2Cq_i+{sC^2q_i^2\over D^2},
\tag{GA.22}
\]

so

\[
\boxed{{B_0\over q_i}=O(1).}
\tag{GA.23}
\]

Singleton safety at `i` says

\[
B_0+2q_ix-q_i^2>0,
\]

hence

\[
\boxed{x>{q_i^2-B_0\over2q_i}=-O(1).}
\tag{GA.24}
\]

Again we derive the opposite bound.

### Case 1: `s>=1/2`

Singleton safety at `j` gives

\[
B_0-2q_jy-q_j^2>0,
\]

and therefore

\[
y<{B_0-q_j^2\over2q_j}=O(1).
\tag{GA.25}
\]

Now

\[
|\delta|
\le |r|\,|w_j-w_i|
=O(1),
\tag{GA.26}
\]

so

\[
x=y-\delta=O(1).
\tag{GA.27}
\]

### Case 2: `s<1/2`

Joint upper-bound violation gives

\[
B_0+2tq_ix-2sq_i\delta-|q_iw_i-q_jw_j|^2\le0.
\tag{GA.28}
\]

Hence

\[
x
\le
{s\over t}\delta
+{|q_iw_i-q_jw_j|^2-B_0\over2tq_i}
\le
{s\over t}\delta
+{|q_iw_i-q_jw_j|^2\over2tq_i}.
\tag{GA.29}
\]

The first term is `O(1)` by (GA.26); the second is `O(q_i)=O(D^-1)`. Thus

\[
x=O(1).
\tag{GA.30}
\]

Together with (GA.24),

\[
\boxed{|r\cdot w_i|=O(1).}
\tag{GA.31}
\]

Since `|r|=D-O(D^-2)` and `|w_i-w_*|=O(D^-1)`,

\[
|r\cdot w_*|=O(1),
\tag{GA.32}
\]

and therefore

\[
\boxed{
d_{\mathbb{RP}^1}([r],[u_*])=O(D^{-1}).}
\tag{GA.33}
\]

---

## 4. Genuine upper binary blockers are globally bounded

Every genuine upper blocker now satisfies uniformly

\[
D-{A\over D^2}\le |xy|<D
\tag{GA.34}
\]

and

\[
d_{\mathbb{RP}^1}([xy],[u_*])\le {L\over D}
\tag{GA.35}
\]

for fixed constants `A,L` independent of the source.

The previously proved parallel-almost-diameters packing lemma states that a unit-separated planar source of diameter `D` contains only

\[
O_{A,L}(1)
\]

such pairs. Its proof uses the diameter bound on cross endpoints to place all chord midpoints and both oriented endpoint populations in fixed-radius disks, followed by unit-separation packing.

Hence

\[
\boxed{
N_{\rm genuine\ binary,upper}=O(1).
}
\tag{GA.36}
\]

In particular the upper shell cannot support a linear or even unbounded-density family of genuinely binary exact-swap interactions.

---

## 5. Genuine lower binary blockers have maximum degree two

Let `G_low` be the graph on source vertices whose edges are all genuine lower binary blockers.

Uniformly, every edge `xy` satisfies

\[
1<|xy|\le1+{A\over D^2}
\tag{GA.37}
\]

and lies within `L/D` projectively of `u_*`.

At a fixed vertex `x`, split incident edges according to whether the ray from `x` lies in the `+u_*` cone or the `-u_*` cone.

Suppose two distinct neighbors `y,z` lie in the same oriented cone. Then

\[
\angle(y-x,z-x)\le{2L\over D},
\]

while both radial lengths lie in `[1,1+A/D^2]`. Therefore

\[
\begin{aligned}
|y-z|
&\le
\big||y-x|-|z-x|\big|
+\max(|y-x|,|z-x|)\,2\sin{L\over D}\\
&\le
{A\over D^2}
+\left(1+{A\over D^2}\right)2\sin{L\over D}
=o(1)<1
\end{aligned}
\tag{GA.38}
\]

for all sufficiently large `D`. This contradicts source unit separation.

Thus there is at most one neighbor in each oriented cone, and

\[
\boxed{\Delta(G_{low})\le2.}
\tag{GA.39}
\]

---

## 6. The lower graph has no cycles

Suppose `G_low` contained a cycle. Choose a cycle vertex `x` maximizing the coordinate

\[
u_*\cdot x.
\tag{GA.40}
\]

Both cycle neighbors `y,z` satisfy

\[
u_*\cdot y\le u_*\cdot x,
\qquad
u_*\cdot z\le u_*\cdot x.
\tag{GA.41}
\]

For sufficiently large `D`, every edge has nonzero `u_*` projection of magnitude at least

\[
|xy|\cos(L/D)>0.
\tag{GA.42}
\]

Hence both rays `y-x` and `z-x` must lie in the same `-u_*` cone. Section 5 permits at most one such neighbor. Contradiction.

Therefore

\[
\boxed{G_{low}\text{ is a forest with maximum degree at most two}.}
\tag{GA.43}
\]

Every nontrivial connected component is a path.

At an internal path vertex, one incident edge lies in the `+u_*` cone and one in the `-u_*` cone. Orienting the path from its minimum to maximum `u_*` coordinate therefore makes every edge point into the `+u_*` cone. Consequently the path vertex order is exactly its order in the common row coordinate.

Thus every genuine lower interaction component is an asymptotically straight row-parallel chain of ultra-near-unit pairs.

---

## 7. Frontier effect

The parity-thinned one-sign strong-TB1 exact-swap system had already been reduced to arity-two inactive constraints. The truth-table theorem then confined all genuinely binary synergy to the `D^-2` shells.

The present theorem removes most of the remaining geometric freedom inside those shells:

```text
genuine binary upper interactions:
    only O(1) source-wide;
    D-O(D^-2) long;
    row-parallel in one O(1/D) cone;
    therefore negligible at positive density.

genuine binary lower interactions:
    1+O(D^-2) long;
    row-parallel in one O(1/D) cone;
    maximum degree two;
    no cycles;
    disjoint monotone path forest.
```

Hence any large genuinely binary coupling in the strong-TB1 branch must be carried by a near-contact path forest running along the common train-row direction.

This still does not close C-II. The remaining finite-swap obstruction can combine this lower path forest with non-shell singleton implications and `q`-descending persistent blockers. The next useful target is to prove that a system blocking every nonzero subset must either contain a linear lower path-forest population, which can then be fused with the path-layer/train geometry, or admit a nonzero exact-swap subset avoiding all inactive violations.
