# Target C-II — shallow-tooth penetration edges form a matching

**Date:** 2026-09-15  
**Repository base:** `d2f0f1280fba2a190cf88e16aa5c9e2e317f8470`  
**Status:** proof-only Type-II strengthening; theorem-state authority unchanged  
**Depends on:** Section-124 fixed-scale near-disk flatness, the shallow-tooth
internal-penetration theorem, and the global-turn shallow-apex theorem  
**LEVEL I STATUS:** `STILL OPEN`

The previous tooth results gave many inward contacts but still treated endpoint
multiplicity cautiously. In the Type-II near-disk branch that caution is unnecessary.
For every fixed shallow threshold with

\[
\alpha_\eta:=\arccos(1-\eta/2)<\pi/6,
\]

the penetration contacts can be chosen to form an actual matching in the unloaded
contact graph:

- different shallow teeth have different apexes;
- different shallow teeth have different inner penetration endpoints;
- no inner endpoint is itself a shallow tooth apex.

At the current low-`t` floor, taking `eta=4/15` gives a matching of size

\[
\boxed{0.4255744656201161781\ldots D-o(D)}.
\]

Thus the matching alone contains more than `0.8511489312D-o(D)` distinct unloaded
vertices.

---

## 1. One-tooth geometry

Let an `eta`-shallow tooth have loaded base `ab`, unloaded apex `x`, and an extra
contact `xw`. Write

\[
|a-b|=2\cos\alpha,
\qquad
0<\alpha\le\alpha_\eta<\pi/6.
\tag{PM.1}
\]

In coordinates whose tangent axis is the base line and whose positive normal points
into the loaded hull,

\[
a=(-\cos\alpha,0),\qquad
b=(\cos\alpha,0),\qquad
x=(0,\sin\alpha).
\tag{PM.2}
\]

The audited internal-penetration theorem proves that every extra contact neighbor of
`x` is unloaded and that

\[
(w-x)\cdot n
>\sin(\pi/3-\alpha).
\tag{PM.3}
\]

Since `|w-x|=1`,

\[
\boxed{
|(w-x)\cdot t|
<\cos(\pi/3-\alpha).
}
\tag{PM.4}
\]

It also gives the absolute local-depth bound

\[
\boxed{
\operatorname{depth}_{ab}(w)>\sqrt3/2.
}
\tag{PM.5}
\]

The apex itself has depth `sin alpha<1/2`.

---

## 2. Type-II flatness removes the last duplicated apexes

The global-turn theorem proves a finite statement valid without using near-disk local
flatness: if `alpha_eta<pi/6`, any apex supporting two shallow teeth forces the two
bases to be adjacent loaded-hull sides and forces the exterior turn at their shared
loaded endpoint to satisfy

\[
\phi\ge\pi-2\alpha_\eta>2\pi/3.
\tag{PM.6}
\]

In Type II this cannot occur for large `D`. Both bases have length at most two, so all
three loaded endpoints lie in one fixed-scale loaded-boundary window. Section 124
fixed-scale flatness says the directions of all loaded-hull sides in such a window
differ by `o(1)`. In particular the exterior turn between the two adjacent bases is
`o(1)`, contradicting (PM.6).

### Lemma PM.1 — Type-II apex injectivity

For every fixed `eta` with `alpha_eta<pi/6`, all sufficiently large Type-II survivors
have pairwise distinct apexes for their `eta`-shallow two-edge outer teeth.

This sharpens the general global-turn bound `A_sh>=N_sh-2` to exact pointwise
injectivity in the near-disk branch.

---

## 3. Fixed-scale hull sides have ordered tangent projections

We use another direct consequence of the same Section-124 flatness. In any fixed
Euclidean neighborhood of one short loaded-hull side, all side directions lie in an
`o(1)` cone around a common oriented tangent `t_0`. Along the corresponding convex
boundary arc, the `t_0` coordinate is therefore strictly monotone for large `D`.

Take two distinct loaded-hull sides `a_1b_1` and `a_2b_2` in such a window. Put

\[
u_i={|a_i-b_i|\over2},
\qquad
M_i={a_i+b_i\over2}.
\]

Their tangent-projection intervals have disjoint interiors and occur in boundary
order, so

\[
\boxed{
|t_0\cdot(M_1-M_2)|
\ge u_1+u_2-o(1).
}
\tag{PM.7}
\]

The `o(1)` accounts only for the `o(1)` difference between physical side length and
its projection onto `t_0`. Intervening hull sides only increase the separation.

---

## 4. Two shallow teeth cannot share an inner endpoint

Take two distinct `eta`-shallow teeth

\[
a_1-x_1-b_1,\qquad a_2-x_2-b_2
\]

and suppose extra contacts from their apexes share one inner endpoint `w`:

\[
|x_1-w|=|x_2-w|=1.
\tag{PM.8}
\]

By Lemma PM.1, `x_1!=x_2`. Every loaded base endpoint lies within distance two of `w`,
so the two bases lie in one fixed-scale loaded-boundary window and (PM.7) applies.

Write

\[
u_i=\cos\alpha_i,
\qquad
r_i=\cos(\pi/3-\alpha_i).
\]

Because each `x_i-M_i` is normal to its own base and the two base directions differ by
`o(1)`,

\[
t_0\cdot(x_i-M_i)=o(1).
\tag{PM.9}
\]

Equation (PM.4), transferred to `t_0`, gives

\[
|t_0\cdot(w-x_i)|<r_i+o(1).
\tag{PM.10}
\]

Therefore

\[
|t_0\cdot(M_1-M_2)|
\le r_1+r_2+o(1).
\tag{PM.11}
\]

Together with (PM.7),

\[
u_1+u_2\le r_1+r_2+o(1).
\tag{PM.12}
\]

But for every `alpha<pi/6`,

\[
\cos\alpha-\cos(\pi/3-\alpha)>0.
\tag{PM.13}
\]

For fixed `eta`, the difference is uniformly positive on
`0<=alpha<=alpha_eta`. Thus (PM.12) is impossible for large `D`.

If the two physical bases coincide, their two endpoint unit circles have exactly one
intersection on the inward side of the loaded supporting line, so the outer-tooth
apexes coincide, already excluded by Lemma PM.1.

### Lemma PM.2 — inner-endpoint injectivity

For every fixed `eta` with `alpha_eta<pi/6`, distinct `eta`-shallow teeth have distinct
inner endpoints for any chosen extra contacts.

In fact the proof shows a stronger statement: one unloaded vertex cannot be an extra
contact neighbor of two different `eta`-shallow tooth apexes.

---

## 5. The two endpoint classes are disjoint

Suppose the inner endpoint `w` of one shallow tooth were itself the apex of another
`eta`-shallow tooth with loaded base `cd`. All four loaded endpoints lie in one
fixed-scale boundary window, so the two support lines have direction and normal offset
differing by `o(1)`.

Relative to the first base, (PM.5) gives

\[
\operatorname{depth}(w)>\sqrt3/2.
\]

Relative to its own shallow base, an apex has depth at most

\[
\sin\alpha_\eta<1/2.
\]

The support-line change is only `o(1)`, leaving a fixed positive contradiction.
Therefore no inner endpoint is a shallow tooth apex.

---

## 6. Penetration matching theorem

Let `N_sh(eta)` be the number of `eta`-shallow two-edge outer teeth. Choose one extra
contact at each shallow apex. Lemmas PM.1 and PM.2 make the outer and inner endpoint
maps injective, and Section 5 makes their images disjoint. Hence the chosen contacts
form a matching `M_eta` with

\[
\boxed{|M_\eta|=N_{sh}(\eta).}
\tag{PM.14}
\]

Every matched edge is internal to one unloaded component, its shallow endpoint has
local depth at most `sin alpha_eta`, and its deep endpoint has local depth greater than
`sqrt(3)/2`.

The metric tooth-detour bound gives

\[
\boxed{
N_{sh}(\eta)
\ge N_2-{d_{out}\over\eta}.
}
\tag{PM.15}
\]

No KKT weight lower bound is used.

---

## 7. Current low-`t` consequence at `eta=4/15`

Take

\[
\boxed{\eta={4\over15}.}
\]

Then

\[
\cos\alpha_\eta={13\over15},
\qquad
\sin\alpha_\eta={2\sqrt{14}\over15},
\qquad
\alpha_\eta<\pi/6.
\tag{PM.16}
\]

The largest allowed tangential component of a penetration edge is

\[
\cos(\pi/3-\alpha_\eta)
={13+2\sqrt{42}\over30}.
\tag{PM.17}
\]

Hence the per-side tangent separation margin used in Lemma PM.2 is

\[
\boxed{
{13\over15}-{13+2\sqrt{42}\over30}
={13-2\sqrt{42}\over30}
=0.0012839534394759846\ldots>0.
}
\tag{PM.18}
\]

It is small but fixed, while the Type-II flatness error is `o(1)`.

At the current proof-only low-`t` floor,

\[
{N_2\over D}
\ge0.4363893718701161781\ldots-o(1),
\qquad
{d_{out}\over D}\le0.002883975+o(1).
\]

Therefore

\[
\boxed{
{|M_{4/15}|\over D}
\ge0.4255744656201161781\ldots-o(1).
}
\tag{PM.19}
\]

The matching has

\[
\boxed{
0.8511489312402323562\ldots D-o(D)
}
\tag{PM.20}

distinct unloaded endpoints. Each matched edge has inward component greater than

\[
\boxed{
Y_{4/15}
={13\sqrt3-2\sqrt{14}\over30}
=0.5011115241615840681\ldots .
}
\tag{PM.21}
\]

---

## 8. Frontier effect

The tooth branch now has a multiplicity-free two-layer form:

```text
>=0.4255744656 D shallow two-edge outer teeth
 -> same number of distinct shallow unloaded apexes
 -> same number of distinct internal unit contacts
 -> same number of distinct deep unloaded endpoints
 -> a matching of size >=0.4255744656 D
    crossing from local depth <0.498888
    to local depth >0.866025.
```

The earlier factor-two endpoint-deduplication loss is completely gone. The next tooth
problem is therefore not counting penetration contacts; it is understanding the
remaining internal degree at the deep matching layer.

C-II remains open.
