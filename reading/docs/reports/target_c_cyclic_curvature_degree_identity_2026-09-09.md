> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_curvature_degree_identity_2026-09-09.md) · source SHA-256 `3fb5eb35674a57ebea2e781fc782ee8d88d399da176809b3bfdde5b2f0971d37`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3A9D6B43EC91","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic equality identifies shell curvature with diameter degree

**Date:** 2026-09-09  
**Run type:** exact local KKT/geometry classification  
**Target:** Target C C-II cyclic primitive endpoint, `d_H=0`  
**Depends on:** CE equal diameter-direction gaps; DC contiguous diameter stars; AS explicit uniform KKT stress  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The CE/DC/AS equality package makes the geometry of every force-hull vertex completely discrete.

Let the shell vertices be

$$
b_0,b_1,\ldots,b_{q-1}
$$

in counterclockwise contact-cycle order. Let

$$
\varphi_i\in(0,\pi)
$$

be the exterior turning angle of the convex unit polygon `F` at `b_i`, and let

$$
d_i:=\deg_H(b_i)
$$

be its degree in the full actual diameter graph.

Then

$$
\boxed{
\varphi_i=\frac{\pi}{q}d_i
\qquad(0\le i<q).
}
\tag{CD.1}
$$

Thus the integer diameter-degree sequence is exactly the curvature sequence of the mechanical shell, measured in quanta `pi/q`.

Equivalently, if `v_i=b_{i+1}-b_i` is the oriented unit side vector, then

$$
\boxed{
\arg v_i-\arg v_{i-1}
=\frac{\pi}{q}d_i
\pmod{2\pi},
}
\tag{CD.2}
$$

with the positive representative in `(0,pi)`.

Consequences:

1. regularity is equivalent to `d_i=2` at every terminal;
2. every diameter leaf (`d_i=1`) carries the minimum curvature `pi/q`;
3. every branching excess `d_i-2>0` is exactly an equal amount of excess turning above the regular value;
4. the leaf/branch balance
   $$
   \sum_i(d_i-2)=0
   $$
   is the ordinary total-curvature identity
   $$
   \sum_i(\varphi_i-2\pi/q)=0.
   $$

This gives a direct bridge between the convex-thrackle caterpillar structure and the Reinhardt sign word: the gaps between consecutive selected side directions of `F` are precisely the diameter degrees.

---

## 1. Contact resultant at one shell vertex

Fix one terminal `b=b_i` and write

$$
p=b_{i-1},
\qquad
c=b_{i+1}.
$$

Both shell sides are unit contacts:

$$
|b-p|=|b-c|=1.
$$

The two contact vectors appearing in KKT equilibrium are

$$
b-p,
\qquad
b-c.
$$

At a strictly convex polygon vertex their mutual angle is

$$
\pi-\varphi_i.
$$

Therefore their vector sum has magnitude

$$
\begin{aligned}
|(b-p)+(b-c)|
&=2\cos\frac{\pi-\varphi_i}{2}\\
&=2\sin\frac{\varphi_i}{2}.
\end{aligned}
\tag{1.1}
$$

AS gives the same contact coefficient on every shell side:

$$
\alpha=\frac{D^2}{q}.
$$

Hence the total contact reaction at `b` has magnitude

$$
\boxed{
|g_b|
=\frac{2D^2}{q}
\sin\frac{\varphi_i}{2}.
}
\tag{1.2}

Its direction is the exterior angle bisector at `b`.

---

## 2. Diameter resultant at the same vertex

Let

\[
d=d_i=\deg_H(b).
$$

DC says all `d` diameter edges incident to `b` form one contiguous block in the cyclic projective diameter-direction order. CE says consecutive projective directions are separated by exactly

$$
\theta:=\frac\pi q.
\tag{2.1}
$$

Orient every incident diameter vector outward at `b`:

$$
b-y,
\qquad y\in N_H(b).
$$

All of these vectors lie in the strict outward normal cone at `b` by the Target C force-hull geometry, so their actual Euclidean directions use the same lift of the projective block. They are therefore `d` radius-`D` vectors with consecutive angular spacing exactly `theta`.

The vector sum of `d` equally spaced unit vectors with spacing `theta` has magnitude

$$
\frac{\sin(d\theta/2)}{\sin(\theta/2)}.
$$

Thus the unweighted diameter-vector sum has magnitude

$$
D\frac{\sin(d\pi/(2q))}{\sin(\pi/(2q))}.
\tag{2.2}
$$

AS gives the uniform normalized diameter coefficient

$$
\beta=\frac1q.
$$

Hence the total diameter reaction has magnitude

$$
\boxed{
|g_b|
=\frac{D}{q}
\frac{\sin(d\pi/(2q))}{\sin(\pi/(2q))}.
}
\tag{2.3}

CE gives

\[
2D\sin\frac\pi{2q}=1,
$$

so (2.3) simplifies to

$$
\boxed{
|g_b|
=\frac{2D^2}{q}
\sin\frac{d\pi}{2q}.
}
\tag{2.4}

The vector direction is the midpoint direction of the contiguous diameter star.

---

## 3. KKT equilibrium forces the turning-degree identity

The AS stress is an exact KKT equilibrium stress. Therefore the contact and diameter resultants in (1.2) and (2.4) are the same vector, in particular have equal magnitude:

\[
\sin\frac{\varphi_i}{2}
=
\sin\frac{d_i\pi}{2q}.
\tag{3.1}
$$

Both arguments lie strictly between zero and `pi/2`.

- Strict convexity gives
  $$
  0<\varphi_i/2<\pi/2.
  $$
- The diameter graph is not a star in the post-ZF regime, so
  $$
  1\le d_i<q,
  $$
  and hence
  $$
  0<d_i\pi/(2q)<\pi/2.
  $$

Sine is strictly increasing on this interval. Therefore (3.1) gives

$$
\boxed{
\varphi_i=\frac\pi q d_i.
}
$$

This proves CD.1. CD.2 is the definition of exterior turning angle. `square`

The direction equality in KKT equilibrium also shows that the midpoint direction of the diameter-star block is exactly the exterior normal bisector at `b`.

---

## 4. Degree sequence equals the side-direction gap sequence

RS says the `q` oriented side vectors of `F` select one member from each antipodal pair of the regular `2q` direction set.

Sort those selected side directions in convex boundary order. The regular direction grid has step

$$
\frac\pi q.
$$

By CD.2, the angular gap from side `v_{i-1}` to side `v_i` is

$$
\frac\pi q d_i.
$$

Therefore exactly `d_i` regular direction-grid steps occur between those consecutive selected side directions.

### Corollary CD.1 — degree composition

The cyclic diameter-degree sequence

$$
(d_0,d_1,\ldots,d_{q-1})
$$

is exactly the cyclic composition of the `2q` regular direction steps determined by the Reinhardt side selection:

$$
\boxed{
 d_i\in\mathbb Z_{>0},
 \qquad
 \sum_{i=0}^{q-1}d_i=2q.
}
\tag{4.1}

The sum identity is simultaneously

- the handshake lemma for `h=q`, and
- total convex turning `2pi`.

Thus the graph and polygon curvature ledgers coincide term by term, not merely after summation.

---

## 5. Leaves and branching are curvature defects

Subtract the regular value two:

\[
\boxed{
\varphi_i-\frac{2\pi}{q}
=\frac\pi q(d_i-2).
}
\tag{5.1}

Sum over all vertices:

\[
\sum_i(d_i-2)=2h-2q=0.
$$

Hence

$$
\boxed{
\sum_{d_i=1}1
=\sum_{d_i\ge3}(d_i-2).
}
\tag{5.2}

for the connected unicyclic diameter graph. This is the familiar leaf/branch excess balance, now with an exact convex-geometric interpretation:

- each leaf removes one curvature quantum `pi/q` below regular;
- a degree-`r` branch adds `r-2` curvature quanta;
- the deficits and excesses cancel because the shell turns exactly once.

For example the degree pattern

\[
3,3,3,1,1,1
$$

has three positive and three negative curvature quanta and is therefore compatible with the total turning constraint; CD does not falsely exclude such branching Reinhardt shells.

---

## 6. Local diagonal consequence

The two contact neighbors `p,c` of `b_i` are separated by

$$
|p-c|
=2\sin\frac{\pi-\varphi_i}{2}
=2\cos\frac{\varphi_i}{2}.
$$

Using CD.1,

$$
\boxed{
|b_{i-1}-b_{i+1}|
=2\cos\frac{d_i\pi}{2q}.
}
\tag{6.1}

Triangle-freeness requires this distance to be strictly greater than one, because equality would make the two shell contacts at `b_i` part of a unit equilateral triangle. Therefore

\[
\boxed{d_i<\frac{2q}{3}.}
\tag{6.2}

C18 gives a substantially stronger asymptotic degree cap through the diameter-star angle, but (6.2) is an exact shell-local consequence requiring no global container estimate beyond the established equality class.

---

## 7. Relation to the DC transition word

In the DC difference-body traversal, a run of consecutive transitions that repeatedly changes the same oriented endpoint corresponds to a diameter star: the unchanged endpoint is shared by all diameter edges in that run.

If the run has `r` transitions, the shared terminal has

\[
d_i=r+1
$$

incident diameter edges. CD says the same vertex has turning angle

$$
\varphi_i=(r+1)\frac\pi q.
$$

Thus branching runs in the transition word, high diameter degree, and large local shell curvature are three descriptions of the same discrete defect.

This is the exact graph-geometric bridge needed to combine future Reinhardt sign-word arguments with diameter-thrackle structure.

---

## 8. Regression audit

### Regular odd shell

All diameter degrees are two. CD gives

$$
\varphi_i=2\pi/q
$$

at every vertex, hence the shell is regular.

### Nonregular composite Reinhardt shell

Allowed. Its nonconstant diameter-degree sequence produces the corresponding nonconstant curvature sequence exactly.

### Abstract DC-compatible branching graph

DC alone permits branching. CD adds the metric requirement that its degree sequence equal the actual shell turning sequence. An abstract interval-neighborhood thrackle with the wrong curvature data is not a CE/AS equality shell.

### Generic positive stress

The uniform coefficients from AS are essential for the simple sine identity. CD is not asserted for arbitrary post-ZF stresses or for `d_H=1,2`.

---

## 9. What this changes

The `d_H=0` equality class now has the exact local dictionary

```text
shell turning at b
    = (pi/q) * diameter degree at b;

diameter-star block width
    = (deg_H(b)-1)pi/q;

Reinhardt side-direction gap
    = deg_H(b) regular direction quanta.
```

Therefore future arithmetic classifications of the RS sign word automatically classify the diameter-degree sequence, and conversely any graph-theoretic restriction on the convex-thrackle degree sequence becomes a curvature restriction on the shell.

---

## 10. Next theorem

The remaining finite equality-class problem can now be phrased without continuous geometry:

> Classify cyclic positive integer sequences `(d_i)` with sum `2q` that simultaneously arise as
> 1. the degree sequence, in contact-cycle order, of the DC convex-thrackle diameter graph, and
> 2. the regular-direction gap composition of a closed `+-1` Reinhardt side word.

A proof that only `d_i=2` survives under the full source/global-minimum hypotheses would reduce the equality branch to the regular odd shell. CD itself does not claim that result.

---

## 11. Promotion recommendation

**Hold as a stacked report.**

CD is exact downstream of CE/DC/AS and the report-level CY endpoint. No canonical file is changed.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In cyclic d_H=0, AS gives uniform normalized stress
    alpha=D^2/q on every shell contact,
    beta=1/q on every diameter edge.
At shell vertex b_i with exterior turning phi_i,
    |contact resultant|
      =(2D^2/q) sin(phi_i/2).
DC+CE make the d_i=deg_H(b_i) incident diameter vectors an equally spaced block
with step pi/q, so
    |diameter resultant|
      =(D/q) sin(d_i pi/(2q))/sin(pi/(2q))
      =(2D^2/q) sin(d_i pi/(2q)).
Equilibrium and monotonicity of sine give
    phi_i=(pi/q)d_i.

Hence the diameter-degree sequence is exactly the curvature/side-direction-gap
composition of the Reinhardt unit shell. Regularity iff all d_i=2. Leaves are one
negative curvature quantum; branches contribute d_i-2 positive quanta.
```
