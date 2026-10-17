> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_universal_force_bulk_closure_2026-09-09.md) · source SHA-256 `6e65184a8574b3f867ad0867dc0c60f81a1f987753d7578b36a36427a93b7494`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EE281D3D6A3A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — all cyclic phases have no external force-hull population

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RP/DC and the `d_H=0` force-bulk work  
**Run type:** exact perimeter-extension contradiction / force-bulk closure  
**Target:** the complete cyclic primitive endpoint, all `d_H=0,1,2`  
**Depends on:** CY cyclic force hull, RP Reinhardt-scale perimeter matching, classical Reinhardt perimeter-diameter inequality  
**External literature:** no new theorem beyond the Reinhardt inequality already used in RP  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The earlier FB theorem proved `A subset F` only in the exact Reinhardt `d_H=0` phase, using the Reuleaux completion and the rattler boundary collar. The following argument is simpler and stronger: near-saturation of the universal Reinhardt perimeter bound makes the cyclic force hull too perimeter-efficient to admit even one source point outside it.

### Theorem UFB — universal cyclic force-bulk closure

For every sufficiently large cyclic primitive survivor, in any of the three phases

$$
d_H\in\{0,1,2\},
$$

the complete source lies in the force hull:

$$
\boxed{A\subseteq F.}
\tag{UFB.1}
$$

Since the `q` force-hull vertices are source points,

$$
\boxed{F=\operatorname{conv}A.}
\tag{UFB.2}
$$

Thus the cyclic endpoint has **no external force-hull rattlers in any topology phase**. All contact-isolated source points are strictly interior to the same convex equilateral `q`-gon whose boundary is the positive contact cycle.

The proof compares two incompatible scales:

- unit separation forces any exterior point to increase convex-hull perimeter by `Omega(1/D)`;
- RP plus Reinhardt leaves only `O(1/D^2)` perimeter headroom, even after allowing one additional hull vertex.

---

## 1. Any exterior source point has height at least `sqrt(3)/2`

Let

$$
x\in A\setminus F
$$

and put

$$
h:=\operatorname{dist}(x,F)>0.
$$

Choose a nearest point

$$
y\in\partial F.
$$

The force hull is a strictly convex polygon with every side of length one.

If `y` is a hull vertex, then unit separation gives immediately

$$
h=|x-y|\ge1.
\tag{1.1}
$$

Otherwise `y` lies in the relative interior of one unit side with endpoints `p_0,p_1`. The segment `xy` is perpendicular to that side. Write the foot coordinate from `p_0` as

$$
s=|p_0-y|\in(0,1).
$$

One endpoint is at tangential distance at most `1/2` from the foot:

$$
\min\{s,1-s\}\le\frac12.
$$

For that endpoint `p`, the right triangle gives

$$
|x-p|^2=h^2+|y-p|^2
\le h^2+\frac14.
$$

Unit separation requires `|x-p|>=1`. Hence

$$
\boxed{h\ge\frac{\sqrt3}{2}.}
\tag{1.2}
$$

This lower bound uses only the prescribed unit boundary sides and source separation; no KKT information is needed.

---

## 2. A point at height `h` forces a quantitative perimeter increase

Let

$$
K:=\operatorname{conv}(F\cup\{x\}).
$$

Since every point of `F` and `x` belongs to the original diameter-`D` source hull,

$$
\operatorname{diam}K\le D.
\tag{2.1}
$$

Let

$$
n:=\frac{x-y}{h}
$$

be the outward unit normal at the nearest point, and choose a unit tangent `t` perpendicular to `n`.

For an angle `phi` with `|phi|<pi/2`, define

$$
u_\phi:=\cos\phi\,n+\sin\phi\,t.
$$

Nearest-point convexity gives

$$
(z-y)\cdot n\le0
\qquad(z\in F).
\tag{2.2}
$$

Also `|z-y|<=D`. Therefore

$$
\begin{aligned}
h_F(u_\phi)
&=\max_{z\in F} z\cdot u_\phi\\
&\le y\cdot u_\phi+D|\sin\phi|.
\end{aligned}
\tag{2.3}
$$

On the other hand

$$
x\cdot u_\phi
=y\cdot u_\phi+h\cos\phi,
$$

so

$$
\boxed{
h_K(u_\phi)-h_F(u_\phi)
\ge
\max\{0,h\cos\phi-D|\sin\phi|\}.}
\tag{2.4}
$$

For a planar convex body, Cauchy's support-function perimeter formula is

$$
\operatorname{per}(L)
=\int_0^{2\pi}h_L(u_\theta)\,d\theta.
\tag{2.5}
$$

Put

$$
a:=\arctan(h/D).
$$

Integrating (2.4) on `[-a,a]` gives

$$
\begin{aligned}
\operatorname{per}(K)-\operatorname{per}(F)
&\ge
2\int_0^a(h\cos\phi-D\sin\phi)\,d\phi\\
&=2\left[h\sin a-D(1-\cos a)\right]\\
&=\boxed{2\left(\sqrt{D^2+h^2}-D\right).}
\end{aligned}
\tag{2.6}
$$

Combining with (1.2),

$$
\boxed{
\operatorname{per}(K)-q
\ge
2\left(\sqrt{D^2+\frac34}-D\right).}
\tag{2.7}
$$

In particular,

$$
\boxed{
\operatorname{per}(K)-q
\ge
\frac{3}{4D}+O(D^{-3}).}
\tag{2.8}
$$

The exact lower bound (2.7), not the expansion, is the proof input.

---

## 3. Reinhardt gives only `O(D^-2)` available perimeter headroom

For an integer `m>=3`, put

$$
U_m(D):=2m\sin\frac\pi{2m}\,D.
\tag{3.1}
$$

Reinhardt's universal theorem says every convex `m`-gon of diameter at most `D` has perimeter at most `U_m(D)`.

The polygon `K` has at most `q+1` vertices. The function

$$
m\mapsto2m\sin\frac\pi{2m}
$$

is increasing, so

$$
\boxed{
\operatorname{per}(K)\le U_{q+1}(D).}
\tag{3.2}
$$

It remains to estimate the headroom

$$
U_{q+1}(D)-q.
$$

### 3.1 Existing `q`-gon headroom

Define the Reinhardt equality diameter for `q` sides by

$$
D_R(q):=\frac1{2\sin(\pi/(2q))}.
\tag{3.3}
$$

Then

$$
U_q(D_R(q))=q.
$$

RP proves in every cyclic phase

$$
\pi D-q
=\frac\pi{24D}+O(D^{-2}).
\tag{3.4}
$$

The elementary expansion of (3.3) gives

$$
\pi D_R(q)-q
=\frac{\pi^2}{24q}+O(q^{-3}).
\tag{3.5}
$$

Since RP also gives `q=pi D+O(D^-1)`, (3.5) becomes

$$
\pi D_R(q)-q
=\frac\pi{24D}+O(D^{-3}).
\tag{3.6}
$$

Subtract (3.6) from (3.4):

$$
\boxed{D-D_R(q)=O(D^{-2}).}
\tag{3.7}
$$

Therefore

$$
\begin{aligned}
U_q(D)-q
&=2q\sin\frac\pi{2q}\,[D-D_R(q)]\\
&=\boxed{O(D^{-2}),}
\end{aligned}
\tag{3.8}
$$

because `2q sin(pi/(2q))=Theta(1)`.

### 3.2 Buying one more polygon vertex also costs only `O(D^-2)`

Extend

$$
f_D(s):=2s\sin\frac\pi{2s}\,D
$$

to real `s>1`. Put `z=pi/(2s)`. Differentiation gives

$$
f_D'(s)
=2D(\sin z-z\cos z).
\tag{3.9}
$$

For small positive `z`,

$$
\sin z-z\cos z=O(z^3).
$$

On the interval `s in [q,q+1]`, RP gives `s=Theta(D)`, hence

$$
f_D'(s)=O(Ds^{-3})=O(D^{-2}).
$$

The mean value theorem yields

$$
\boxed{U_{q+1}(D)-U_q(D)=O(D^{-2}).}
\tag{3.10}
$$

Combining (3.8) and (3.10),

$$
\boxed{U_{q+1}(D)-q=O(D^{-2}).}
\tag{3.11}
$$

---

## 4. Contradiction

If an exterior source point existed, (2.7) and (3.2) would give

$$
2\left(\sqrt{D^2+\frac34}-D\right)
\le
U_{q+1}(D)-q.
\tag{4.1}
$$

The left side is

$$
\frac{3}{4D}+O(D^{-3}),
$$

while the right side is `O(D^-2)` by (3.11).

For sufficiently large `D` this is impossible.

Therefore no source point lies outside `F`. This proves UFB.1-UFB.2. `square`

---

## 5. Consequences in each cyclic phase

### `d_H=0`

UFB reproves the earlier FB force-bulk closure without using the Reuleaux completion or RD boundary-depth theorem. The stronger RE/RC/RD geometry remains useful for the exact equality-family analysis.

### `d_H=1`

DC says the full diameter graph is one spanning tree. UFB now adds

$$
F=\operatorname{conv}A.
$$

Thus the entire quadratic source population is inside the same equilateral force polygon on which TC/WT analyze the KKT endpoints.

### `d_H=2`

DC/D2 say the full diameter graph is two ordered caterpillar components on four alternating blocks. UFB again gives

$$
F=\operatorname{conv}A.
$$

So the unique-stress four-block endpoint also has no external population escape.

The previously separate cyclic topology and population programs are now on the same geometric hull in all three cases.

---

## 6. Direct source-capacity consequence

Because `F=conv A`, Oler applies directly to the complete source in every cyclic phase:

$$
\boxed{
n\le\frac2{\sqrt3}\operatorname{area}(F)+\frac q2+1.}
\tag{6.1}
$$

Likewise, every finite disk-packing theorem stated in terms of the convex hull of the center set can now be applied directly to `F` throughout the cyclic endpoint, not only in the exact Reinhardt subphase.

In particular, the Wegner insertion from WG extends formally to all cyclic phases once only `F=conv A` and `per(F)=q` are used; its `d_H=0` Reuleaux-core corollaries remain phase-specific.

---

## 7. Regression audit

### Exterior point directly above a unit side midpoint

The height threshold `sqrt(3)/2` is sharp for unit separation from the two side endpoints. The exact support-function perimeter lower bound then gives the smallest possible cost used by UFB.

### Exterior point nearest a vertex

Its height is at least one, producing an even larger perimeter increase.

### Hull chain replacement

Adding `x` may hide several old force-hull vertices. No assumption that `K` has exactly `q+1` vertices is used: it has at most `q+1`, and the Reinhardt upper is monotone in the allowed vertex count.

### Non-Reinhardt `d_H=1,2`

Exact Reinhardt equality is not assumed. RP's `O(D^-2)` distance to the universal `q`-gon perimeter bound is enough.

### C1/C65 normalization warning

UFB does not combine contact-preserving diametral hull saturation with the C65 lexicographic source. It works directly on the C65 cyclic source using only its existing force hull and RP. Thus it does not violate the promoted warning in `56-ci-restored-frontier.md`.

---

## 8. What this changes

The full cyclic endpoint now has a common source-wide geometry:

```text
F = conv(A)
per(F)=q
C positive core = unit boundary cycle C_q
all n-q contact-isolated C65 points lie strictly inside F
q = pi D - pi/(24D) + O(D^-2)
```

The only remaining topology split is in the diameter graph/stress family:

```text
d_H=0: one odd-unicyclic caterpillar, 2D KKT polytope, exact Reinhardt equality (RE)
d_H=1: one spanning tree, 1D KKT segment, TC endpoint parallelograms
d_H=2: two four-block caterpillar trees, unique KKT stress, D2 parallelogram
```

There is no longer a cyclic external-rattler branch.

---

## 9. Next theorem

The highest-value population target is now common to all three phases:

> sharpen Oler/Wegner for a unit-separated set whose complete convex hull is a strictly convex equilateral unit `q`-gon with `q=pi D-pi/(24D)+O(D^-2)`.

The highest-value topology targets remain TC+WT for `d_H=1` and D2 equal-diameter four-block geometry for `d_H=2`.

Because UFB places the full population inside the same hull, either kind of theorem can now use source density without a representative/localization gap.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The perimeter-extension lemma is elementary. The only nonlocal input is report-level RP; its classical Reinhardt dependency was already imported there.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Suppose x is a source point outside the cyclic force hull F. Let h=dist(x,F).
Because every hull side has length 1 and x is unit-separated from its endpoints:
  h>=sqrt(3)/2.

For K=conv(F union {x}), nearest-point support geometry gives
  per(K)-per(F)
    >= 2(sqrt(D^2+h^2)-D)
    >= 2(sqrt(D^2+3/4)-D)
    = 3/(4D)+O(D^-3).

K has at most q+1 vertices and diameter <=D. Reinhardt gives
  per(K)<=U_{q+1}(D),
  U_m(D)=2m sin(pi/(2m))D.
RP says
  pi D-q=pi/(24D)+O(D^-2).
Comparing to the q-gon Reinhardt equality diameter D_R(q) gives
  D-D_R(q)=O(D^-2),
so
  U_q(D)-q=O(D^-2).
Also by differentiating U_s,
  U_{q+1}(D)-U_q(D)=O(D^-2).
Hence
  U_{q+1}(D)-q=O(D^-2),
contradicting the Omega(1/D) perimeter cost above.

Therefore for every cyclic phase d_H=0,1,2:
  A subset F,
  F=conv(A).
No external cyclic rattlers remain.
```
