# Erdos Problem #99 - loaded flat-center singleton unloading gate

**Date:** 2026-09-14
**Target:** C-II, canonical contact-minimal full-core Type-II branch
**Dependencies:** low-t flat-center amplification; global flat-center stress trichotomy; exact stopped-train singleton/rhombic decomposition; independently audited explicit rhombic-train gap
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The current low-`t`, small-residual branch contains almost `0.4944D` distinct flat
pentagon centers at the proof-only endpoint. The global flat-center trichotomy leaves
three possibilities: loaded degree-two centers, unloaded degree-three centers, or
unloaded degree-four centers.

The loaded class has an additional exact cost that was not used in that trichotomy.
A loaded flat center is a convex-hull extreme point and has contact degree exactly two.
Its two contact edges bound the flat pentagon on one side. The other side of each edge
is the actual outer face. Hence both edges are singleton stopped trains touching that
pentagon. Distinct loaded flat centers consume distinct such singleton trains.

Thus, if `L` is the loaded flat-center set and `S` is the total singleton stopped-train
population,

\[
\boxed{2|L|\le S.}
\tag{LU.1}
\]

This converts the existing lower bound on flat-center population and the existing
upper bound on total singleton population into an **unconditional unloaded-center
floor**.

Put

\[
\Delta_2={\pi\over2\sqrt3},\qquad
s:=\sqrt{\Delta_2},\qquad
C_0:=2s+0.00042,
\]

and on a convergent Type-II subsequence write

\[
t:=\lim{q-k\over D},\qquad
\delta:=\lim{b-P_F\over D},\qquad
\kappa:=\lim{k\over D}.
\]

Assume

\[
R_F=o(D).
\tag{LU.2}
\]

The low-`t` flat-center theorem gives

\[
{V_{flat}\over D}
\ge
P(t,\delta,\kappa)-o(1),
\qquad
P(t,\delta,\kappa)
:=\pi+C_0-{5t\over2}+\delta+{\kappa\over2}.
\tag{LU.3}
\]

Let `U=U_3\sqcup U_4` be the unloaded flat centers. Using the independently audited
explicit rhombic-train gap

\[
\liminf {T_R\over D}\ge2s+0.0004,
\tag{LU.4}
\]

we prove

\[
\boxed{
\liminf { |U|\over D}
\ge
U_*(t,\delta,\kappa),
}
\tag{LU.5}
\]

where

\[
\boxed{
U_*(t,\delta,\kappa)
:=2\pi+3s+0.00062-5t+2\delta+{\kappa\over2}.
}
\tag{LU.6}
\]

Whenever the right side is positive, the loaded branch can no longer be the sole flat
center escape.

At the current proof-only floor

\[
t_{42}
={4\over9}(\pi+s)+0.0013751
=1.8208886379794447\ldots,
\]

after conservatively dropping the nonnegative `delta,kappa` bonuses,

\[
\boxed{
\liminf {|U|\over D}
\ge0.0363005378742349\ldots .
}
\tag{LU.7}
\]

The coefficient remains positive for

\[
\boxed{
t<1.8281487455542917\ldots}
\tag{LU.8}
\]

before using any `delta,kappa` bonus.

Combining (LU.5) with the already-proved degree-three/degree-four consequences gives a
strict two-way endpoint fork. If `U_*(t,delta,kappa)>0`, then at least one of:

1. there is a pairwise endpoint-disjoint inactive-pair family `H_4` with
   \[
   \boxed{
   \liminf {|H_4|\over D}
   \ge {U_*(t,\delta,\kappa)\over9},
   }
   \tag{LU.9}
   \]
   and total hidden-side excess `o(D)`; or
2. there is a set `E_3` of distinct positive contact edges with
   \[
   \boxed{
   \liminf {|E_3|\over D}
   \ge {U_*(t,\delta,\kappa)\over4},
   }
   \tag{LU.10}
   \]
   and total normalized KKT weight `o(D^2)`.

At `t=t_42`, `delta=kappa=0`, this is

\[
\boxed{|H_4|/D\ge0.00403339309713722\ldots-o(1)}
\tag{LU.11}
\]

or

\[
\boxed{|E_3|/D\ge0.00907513446855875\ldots-o(1).}
\tag{LU.12}
\]

The constants are smaller than the conditional branches in the three-way stress
trichotomy because (LU.9)--(LU.12) are unconditional after the loaded class is paid by
the finite singleton population.

---

## 1. A loaded flat center produces two singleton trains

Let `P` be a sufficiently flat good pentagon with distinguished center `m` and
consecutive face contacts

\[
l-m-r,
\qquad
\angle lmr\ge\pi-\epsilon_D,
\qquad \epsilon_D\to0.
\]

Suppose `m` is positively diameter-loaded. The global flat-center theorem proves

\[
\deg_C(m)=2.
\tag{LU.13}
\]

So `ml,mr` are the only contact edges incident with `m`.

The pentagon `P` occupies the bounded face sector between these two edges. The other
sector at `m` has angle

\[
2\pi-\angle lmr>\pi.
\]

A loaded source vertex is an extreme point of the source convex hull. At a hull vertex,
every bounded contact-face angle is contained in the strictly smaller-than-`pi` hull
interior angle. Therefore the complementary `>pi` sector cannot be a bounded face. It
is the actual outer face.

Consequently each of `ml,mr` has

```text
flat pentagon on one side,
actual outer face on the other side.
```

Neither edge can lie in a strict rhombus, so each is a singleton stopped train. Both
singletons have a bounded exceptional-face terminal occurrence and hence are counted
by the exceptional singleton population `S_E` as well as by the total singleton
population `S`.

For sufficiently small flatness tolerance the equality trapezoid has a unique
near-straight center, and stability preserves that uniqueness. A singleton edge just
described has only one bounded incident face, namely `P`; therefore it cannot be one of
the two center edges assigned to a different loaded good pentagon. Thus the two
singleton trains are distinct across loaded centers, proving the stronger finite bound

\[
\boxed{2|L|\le S_E\le S.}
\tag{LU.14}
\]

---

## 2. Upper bound the total singleton population

Write

\[
T=T_R+S
\tag{LU.15}
\]

for the exact all-train decomposition into non-singleton rhombic trains and singleton
trains.

The exact terminal-occurrence ledger is

\[
2T=b+Q+4f.
\tag{LU.16}
\]

Every bounded exceptional face has degree at least five, so `f<=Q`. Hence

\[
2T\le b+5Q.
\tag{LU.17}
\]

The exact outer/exceptional endpoint identity is

\[
b+Q=2(q-k).
\tag{LU.18}
\]

On the Type-II limit,

\[
{b\over D}\to\pi+\delta,
\qquad
{Q\over D}\to2t-\pi-\delta.
\]

Substitution in (LU.17) gives

\[
\limsup {T\over D}
\le5t-2\pi-2\delta.
\tag{LU.19}
\]

The independently audited explicit rhombic-train theorem gives (LU.4). Combining
(LU.15), (LU.19), and (LU.4),

\[
\boxed{
\limsup {S\over D}
\le
5t-2\pi-2\delta-2s-0.0004.
}
\tag{LU.20}
\]

Therefore (LU.14) yields

\[
\limsup {|L|\over D}
\le
{5t\over2}-\pi-\delta-s-0.0002.
\tag{LU.21}
\]

---

## 3. Subtract the loaded capacity from the flat-center sea

The distinct flat-center population from (LU.3) partitions as

\[
V_{flat}=L\sqcup U_3\sqcup U_4.
\]

Thus

\[
|U|=|U_3|+|U_4|=|V_{flat}|-|L|.
\]

Using the lower bound (LU.3) and upper bound (LU.21),

\[
\begin{aligned}
\liminf {|U|\over D}
&\ge
\pi+C_0-{5t\over2}+\delta+{\kappa\over2}
-\left({5t\over2}-\pi-\delta-s-0.0002\right)\\
&=2\pi+C_0+s+0.0002-5t+2\delta+{\kappa\over2}\\
&=2\pi+3s+0.00062-5t+2\delta+{\kappa\over2},
\end{aligned}
\]

which is (LU.5)--(LU.6).

At `t=t_42`, direct substitution gives (LU.7). Solving

\[
2\pi+3s+0.00062-5t=0
\]

gives (LU.8).

---

## 4. Remove the loaded class from the global trichotomy

The unloaded set is the disjoint union `U_3\sqcup U_4`, so one class has size at least
`|U|/2`.

If

\[
|U_4|\ge {|U|\over2},
\]

the existing degree-four activation theorem gives an endpoint-disjoint hidden-pair
family

\[
|H_4|\ge {2|U_4|\over9}\ge {|U|\over9}.
\]

Its inherited activation budget has total hidden-side excess `o(D)` on the same
small-residual diagonal scale. This proves (LU.9).

If instead

\[
|U_3|\ge {|U|\over2},
\]

the global flat-center stress theorem assigns one exterior positive contact to each
center and deduplicates with loss at most two:

\[
|E_3|\ge {|U_3|\over2}\ge {|U|\over4}.
\]

The same theorem gives

\[
\sum_{e\in E_3}\alpha_e=o(D^2)
\]

for the normalized relative-interior KKT stress. This proves (LU.10).

At `t_42`, divide the coefficient in (LU.7) by `9` and `4` to obtain
(LU.11)--(LU.12).

---

## 5. Frontier effect

Near the present scalar floor, the loaded flat-center sea is no longer a complete
escape. The finite singleton-train budget forces a linear unloaded remainder:

```text
>= 0.0363005 D unloaded flat centers
    -> either >= 0.00403339 D endpoint-disjoint near-active hidden pairs
       with o(D) total activation gap,
    -> or >= 0.00907513 D distinct positive contacts
       with o(D^2) total KKT weight.
```

Thus the narrow endpoint `t<1.8281487455...` is reduced to two source-level
degeneracies. Excluding both would immediately raise the proof-only `q-k` floor from
`t_42=1.8208886...` to at least `1.8281487...`, before using positive `delta` or
`kappa` bonuses.

This note does not exclude either degeneracy. Near contacts do not activate by
compactness alone, and a linear low-stress contact family is not inconsistent with a
relative-interior finite KKT stress. C-II and Level I remain open.

## 6. Scope audit

- The singleton/rhombic decomposition is occurrence-counted and includes all singleton
  stopped trains, not only bridges.
- (LU.14) does not assume a singleton edge is a bridge. It uses only the two incident
  face sides of a degree-two loaded center.
- The loaded-center degree-two input is the current global flat-center theorem.
- The upper singleton bound uses the independently audited `0.0008D` rhombic train
  slack, not the newer larger proof-only phase-star constant.
- The low-`t` flat-center population and `R_F=o(D)` remain proof-only inputs awaiting
  their own audit chain.
- Contact-isolated source points remain in the full source.
- No exact unit equilateral triangle or same-cardinality strict sub-`D` source is
  produced.
