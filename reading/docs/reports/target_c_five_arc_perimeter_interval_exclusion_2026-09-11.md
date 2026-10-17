> Generated reading edition · [exact source](../../../docs/reports/target_c_five_arc_perimeter_interval_exclusion_2026-09-11.md) · source SHA-256 `148fd583fed1ea69c1235203239fda1b3d7ef623cbe4fabead1d8f9ffb6159e4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DE9E6E3F288D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Five-arc attachment phase: a full interval excluded by perimeter capacity

**Date:** 2026-09-11  
**Status:** proved conditional branch theorem; unpromoted  
**Target:** Target C, C-II high-surplus attachment phase

## Result

The attachment-perimeter capacity theorem (APC) excludes more than the single
endpoint (z_*).  Let (I_D) be an unloaded positive-contact component with


```text
diam_C(I_D)/D -> z,
```

and suppose its actual loaded attachment directions occupy all five components
of the first five-component maximal wrapping set.  Put


```text
phi(z) = pi - 2 asin(z),
M_5(z) = 10 asin(z) - 4 pi.
```

For


```text
sin(2 pi/5) < z < sin(3 pi/7),
```

there is a unique (z^dagger) satisfying


```text
10 z sqrt(1-z^2) = 4 M_5(z),
```

with


```text
z^dagger = 0.9680478474... .
```

No such five-arc component can have (z<z^dagger).  In particular, the
previous endpoint exclusion at (z_*=0.9604607492ldots) extends through the
entire interval


```text
z_* <= z < z^dagger.
```

The decimal value is diagnostic only; the theorem uses the uniquely defined
root.  This remains a branch theorem, not a C-II settlement, because a survivor
may use three wrapping components or a later (7,9,ldots)-component phase.

## Inputs and exact hypotheses

Use the following already proved report-level inputs.

1. **Attachment diameter/pin bound.**  For (a_D=|A_D|), where (A_D) is the
   distinct loaded attachment set,

   
   ```text
   diam_C(I_D) <= 3 a_D - 3.
   ```

   Hence (a_D/Dge z/3+o(1)).  This lower bound is not used in the new
   contradiction except to identify the relevant macroscopic phase.

2. **Pin-to-direction injection.**  Because (z<1), two distinct attachment
   points cannot use the same actual diameter edge: their Euclidean distance is
   at most (operatorname{diam}_C(I_D)+2<D).  Thus the selected incident
   diameter directions are distinct.

3. **Projective separation and force-side center.**  The selected directions
   are (2arcsin(1/(2D)))-separated and differ by (o(1)) in angle from the
   polar directions of the attachments about the full-source center.  Therefore,
   if they lie in a projective host set of measure (M_5(z)+o(1)),

   
   ```text
   a_D/D <= M_5(z) + o(1).
   ```

4. **APC.**  The convex attachment hull satisfies

   
   ```text
   per(conv A_D) <= 4 a_D - 6.
   ```

5. **Five-arc geometry.**  The five occupied components are separated, in the
   ordinary angular lift, by five gaps of size at least (2phi(z)+o(1)).

These hypotheses deliberately include actual five-arc occupancy.  Merely having
five components in an inclusion-maximal *extension* is not enough unless the
actual attachment directions occupy them.

## Proof

Set


```text
z_5 = sin(2 pi/5),    z_7 = sin(3 pi/7).
```

For (z_5<z<z_7),


```text
pi/7 < phi(z) < pi/5.
```

The five host gaps have total angular length (2pi).  If (g_i) are the five
actual cyclic gaps joining consecutive occupied host components, then


```text
g_i >= 2 phi(z) + o(1).
```

Moreover, for every (i),


```text
g_i <= 2 pi - 8 phi(z) + o(1) < pi + o(1),
```

because (phi(z)>pi/7>pi/8).  All five gaps therefore lie in the range
where the chord function is increasing.  The five corresponding attachment-hull
chords have lengths


```text
D sin(g_i/2) + o(D) >= D sin(phi(z)) + o(D).
```

The attachments are vertices of a strictly convex force hull, so these chords
are sides of (operatorname{conv}A_D), possibly with additional attachment
vertices and sides between them.  Consequently


```text
liminf per(conv A_D)/D >= 5 sin(phi(z))
                              = 10 z sqrt(1-z^2).
```

On the other hand, the five-component host set has projective measure


```text
M_5(z) = 10 asin(z) - 4 pi.
```

The separated pin directions lie in that host set up to (o(1)), so


```text
limsup a_D/D <= M_5(z).
```

APC now gives


```text
limsup per(conv A_D)/D <= 4 M_5(z).
```

Thus a five-arc component requires


```text
F(z) := 10 z sqrt(1-z^2) - 4(10 asin(z)-4 pi) <= 0.       (1)
```

But


```text
F'(z) = -(30 + 20 z^2)/sqrt(1-z^2) < 0.
```

At (z=z_5), (M_5(z_5)=0), so (F(z_5)>0).  At (z=z_7),


```text
M_5(z_7) = 2 pi/7,
10 z_7 sqrt(1-z_7^2) = 5 sin(pi/7) < 5 pi/7 < 8 pi/7 = 4 M_5(z_7).
```

Hence (F(z_7)<0), and strict monotonicity gives a unique root
(z^daggerin(z_5,z_7)).  Inequality (1) is impossible for
(z<z^dagger).  This proves the theorem. (square)

## Relation to the earlier endpoint theorem

The delayed-five-arc theorem gives (z_*=0.9604607492ldots) from the pin
density condition (M_5(z)ge z/3).  Since


```text
z_* < z^dagger,
```

the new result rules out the whole five-arc interval immediately above the first
permitted endpoint, not only convergence to (z_*).  At (z=z^dagger) the
perimeter inequalities can meet, so equality is not excluded by this argument.

## Exact surviving obstruction

This does not prove that every low-(z) survivor is impossible.  The following
cases remain distinct and are not silently merged:

* a three-component attachment phase, which is not subject to the five-arc
  perimeter lower bound;
* a five-component phase with (zge z^dagger);
* later odd-component wrapping phases;
* (s_Z>0), cyclic/forest (s_Z=0) branches not represented by this one
  attachment cell; and
* contact-isolated source points.

The theorem therefore changes the five-arc endpoint ledger but leaves the global
population/response contradiction unresolved.
