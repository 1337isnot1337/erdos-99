> Generated reading edition · [exact source](../../../docs/reports/target_c_contact_minimal_annular_chamber_2026-09-10.md) · source SHA-256 `e5a485df4024bd45c4aaa640b695d884cbb4c523b3e982a65d3b285c2255c2ef`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-16F9A673BB82","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — contact minimality forces a macroscopic isolated annular chamber

**Date:** 2026-09-10  
**Repository state:** draft PR #178 after WG commit `b479df91df653a1b67ee52e3a37a3d795f6ba746`; current `main` includes `ff31de4783ff49173d9f4bfdf61364735ff5a590`  
**Run type:** exact finite-capacity / source-population reduction  
**Target:** Target C, C-II with all contact-isolated points retained  
**Depends on:** contact-minimal representative; C65 full force visibility; PI force-perimeter envelope; whole-source Oler/lattice allowance  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The low-surplus annulus can be localized much more strongly than the earlier global
population estimates suggest.

Contact minimality itself gives a finite covering certificate: deleting any
nonisolated contact vertex leaves closed unit disks around the remaining source points
that cover the entire source hull.  Since the whole nonisolated force-visible contact
core lies in the force hull `F`, the part of the source hull more than unit distance
from `F` must be covered entirely by contact-isolated source points.

Combining this with the explicit PI force-perimeter deficit gives a macroscopic disk
inside `K\setminus F`.  A concentric disk of almost the same radius is therefore
unit-covered by contact-isolated source points.  Quantitatively, for every fixed

```math
\lambda_0<\lambda_{\rm disk},
\qquad
\lambda_D:=\frac{e_{BB}+2s_C}{D},
```

there is `tau(lambda_0)>0` such that every sufficiently large post-ZF survivor with
`lambda_D<=lambda_0` contains a point `x` for which

```math
\boxed{B(x,\tau D)\subset K\setminus F,}
\tag{CM.1}
```

and at least

```math
\boxed{(\tau D-1)^2}
\tag{CM.2}
```

contact-isolated source points lie in `B(x,tau D)` and their closed unit disks cover
`B(x,tau D-1)`.

Thus the isolate-heavy branch contains a **macroscopic core-free Delone chamber**,
not merely a quadratic number of rattlers distributed somewhere in the annulus.
This removes force-core exterior compatibility from any finite rearrangement whose
support is `o(D)` and is placed well inside the chamber.

---

## 1. Contact-minimal deletion covering

Let `A` be a triangle-free global minimizer of diameter `D=D(n)` chosen with the
minimum possible number of unit contacts, and put

```math
K=\operatorname{conv}A.
```

### Theorem CM.1 — deletion covering

For every nonisolated contact vertex `v in A`,

```math
\boxed{
K\subseteq
\bigcup_{a\in A\setminus\{v\}}\overline B(a,1).
}
\tag{1.1}
```

### Proof

Assume there were `x in K` such that

```math
|x-a|>1
\qquad(a\in A\setminus\{v\}).
\tag{1.2}
```

Replace `v` by `x`:

```math
A'=(A\setminus\{v\})\cup\{x\}.
```

All pairwise separations in `A'` are at least one, and every pair involving `x` is
strictly longer than one.  Since every point of `A'` lies in the convex body `K` and
`diam K=D`,

```math
\operatorname{diam}A'\le D.
```

By the definition of `D(n)`, equality must hold, so `A'` is again a global minimizer.
It is triangle-free because no new unit contact is incident to `x`.  Every original
contact incident to `v` has disappeared, and `v` was nonisolated, so the total number
of contacts has strictly decreased.  This contradicts the choice of `A`.  Therefore
(1.1) holds. `square`

This theorem uses the global minimum only to turn `diam A'<=D` into another minimizer;
contact minimality then supplies the contradiction.  No infinitesimal motion or KKT
argument is involved.

### Corollary CM.2 — the deep exterior is covered only by isolates

Work now in C-II after C65.  Let `C_core` be the unique nonisolated positive contact
core and let

```math
F=\operatorname{conv}B_+
```

be the force hull of the actual diameter endpoints.

Every vertex of `C_core` lies in `F`.  Indeed, at every unloaded core vertex KKT
equilibrium writes that vertex as a strict positive convex combination of its contact
neighbors.  Applying the discrete maximum principle to every linear functional on the
connected positive contact network places all unloaded vertices in the convex hull of
the loaded vertices `B_+`.  C65 identifies those loaded vertices with the actual
diameter endpoints.

Let `Z` be the set of contact-isolated source points.  Then CM.1 implies

```math
\boxed{
\{y\in K:\operatorname{dist}(y,F)>1\}
\subseteq
\bigcup_{z\in Z}\overline B(z,1).
}
\tag{1.3}
```

To see this, choose any contact vertex `v`.  For a point `y` on the left, CM.1 gives
`a in A\setminus\{v\}` with `|y-a|<=1`.  Such an `a` cannot belong to `F`; otherwise
`dist(y,F)<=1`.  Since the entire nonisolated contact core is contained in `F`, `a`
must be contact-isolated. `square`

This is a finite source-capacity statement absent from the regular-shell and arbitrary
dense-filling regressions: it follows specifically from the contact-minimal global
representative.

---

## 2. A macroscopic ball lies between the source and force hulls

Fix

```math
\lambda_0<\lambda_{\rm disk}.
```

Let `p_+(lambda)` be the explicit perimeter envelope from PI.  Put

```math
p_0:=p_+(\lambda_0)<\pi,
\qquad
p_1:=\frac{\pi+p_0}{2}<\pi,
\tag{2.1}
```

and

```math
\eta_0:=
\frac\pi4-\frac{p_1^2}{4\pi}
=\frac{\pi^2-p_1^2}{4\pi}>0.
\tag{2.2}
```

PI implies that for all sufficiently large post-ZF survivors with
`lambda_D<=lambda_0`,

```math
\operatorname{per}F\le p_1D.
\tag{2.3}
```

For the full source hull the exact Oler/lattice allowance gives

```math
0\le\delta_K
:=\frac\pi4D^2-\operatorname{area}K
<\frac{\sqrt3}{4}\operatorname{per}K
\le\frac{\pi\sqrt3}{4}D.
\tag{2.4}
```

Hence

```math
\operatorname{area}K
\ge\frac\pi4D^2-O(D).
\tag{2.5}
```

By isoperimetry and (2.3),

```math
\operatorname{area}F
\le\frac{p_1^2}{4\pi}D^2.
\tag{2.6}
```

Thus, after increasing the threshold in `D`,

```math
\boxed{
\operatorname{area}(K\setminus F)
\ge\frac{\eta_0}{2}D^2.
}
\tag{2.7}
```

Set

```math
\boxed{
\tau:=\frac{\eta_0}{12\pi}>0.
}
\tag{2.8}
```

### Lemma CM.3 — boundary-layer estimate

For nested compact convex planar bodies `F subseteq K` and every `r>0`, if every point
of `K\setminus F` is within distance `r` of `F` or within distance `r` of `partial K`,
then

```math
\boxed{
\operatorname{area}(K\setminus F)
\le
r\bigl(\operatorname{per}K+\operatorname{per}F\bigr)+\pi r^2.
}
\tag{2.9}
```

### Proof

The portion within distance `r` of `F` is contained in

```math
(F+r\mathbb B)\setminus F,
```

whose area is exactly

```math
r\operatorname{per}F+\pi r^2
```

by Steiner's formula.

For the inner boundary layer of `K`, let

```math
K_{-t}:=\{x:x+t\mathbb B\subset K\}.
```

The coarea formula for the distance to `partial K`, together with monotonicity of
perimeter under inclusion for convex bodies, gives

```math
\operatorname{area}\{x\in K:\operatorname{dist}(x,\partial K)<r\}
\le
\int_0^r\operatorname{per}(K_{-t})\,dt
\le r\operatorname{per}K.
```

Adding the two layers proves (2.9). `square`

### Theorem CM.4 — macroscopic core-free chamber

For all sufficiently large survivors with `lambda_D<=lambda_0`, there exists
`x=x_D` such that

```math
\boxed{
\operatorname{dist}(x,F)\ge\tau D,
\qquad
\operatorname{dist}(x,\partial K)\ge\tau D.
}
\tag{2.10}
```

In particular the open disk `B(x,tau D)` lies in `K\setminus F`.

### Proof

Assume no such point exists and apply CM.3 with `r=tau D`.  Since both `K` and `F`
have diameter at most `D`, Cauchy's perimeter--diameter inequality gives

```math
\operatorname{per}K,\operatorname{per}F\le\pi D.
```

Therefore

```math
\operatorname{area}(K\setminus F)
\le
(2\pi\tau+\pi\tau^2)D^2.
\tag{2.11}
```

From (2.2), `eta_0<pi/4`, hence `tau<1/48<1`; consequently

```math
2\pi\tau+\pi\tau^2<3\pi\tau=\frac{\eta_0}{4}.
```

This contradicts (2.7). `square`

The constants are deliberately conservative.  The theorem needs only a fixed positive
linear chamber radius.

---

## 3. The chamber contains quadratically many isolated source points

Let

```math
r:=\tau D.
```

For large `D`, `r>1`.  By CM.4,

```math
B(x,r)\cap F=\varnothing,
\qquad
B(x,r)\subset K.
\tag{3.1}
```

Apply CM.2 to every `y in B(x,r-1)`.  There is a contact-isolated source point `z`
with `|y-z|<=1`.  The triangle inequality gives

```math
|z-x|<r,
```

so in fact `z in B(x,r)`.

Thus, with

```math
Z_x:=Z\cap B(x,r),
```

we have the exact covering

```math
\boxed{
B(x,r-1)
\subseteq
\bigcup_{z\in Z_x}\overline B(z,1).
}
\tag{3.2}
```

Taking areas and using subadditivity,

```math
\pi(r-1)^2
\le |Z_x|\pi.
```

Therefore

```math
\boxed{|Z_x|\ge(r-1)^2=(\tau D-1)^2.}
\tag{3.3}
```

Every pair of points of `Z_x` has distance strictly larger than one because all of
these source points are contact-isolated.

Hence `Z_x` is simultaneously

- a strict unit-separated packing;
- a unit-radius covering of `B(x,r-1)`;
- contained in the core-free disk `B(x,r)`;
- of cardinality `Omega_{lambda_0}(D^2)`.

This is the announced macroscopic isolated chamber.

---

## 4. Exact target effect

Before CM, the low-surplus branch allowed the quadratic external-isolate population to
be geometrically diffuse and arbitrarily entangled with the force-visible core.
CM removes that possibility.  There is a disk of radius `Theta(D)` containing only
contact-isolated source points and separated by `Theta(D)` from both the force hull and
the outer source boundary.

Therefore any finite rearrangement supported in a ball of radius `o(D)` inside the
central part of this chamber has automatic compatibility with the force-visible core
and with `partial K`.  The remaining obstruction is entirely internal to the isolated
packing: the strict pairwise gaps may be arbitrarily small, so no current theorem gives
an `o(D)` support bound for a positive-cardinality rearrangement.

This is precisely where the Kuperberg gap-defect theorem is near but not yet enough.
The audited Target A five-block theorem gives support

```math
W(d)\le C_1\exp(C_2d^{-3})
```

for an aligned lattice gap of width `d`, but CM supplies neither an aligned triangular
lattice phase nor a quantitative lower bound on the minimum strict gap.  Importing the
five-block move without those two hypotheses would be invalid.

---

## 5. Regressions and adversarial audit

### Regular odd shell

The shell lies outside the PI low-surplus branch, so CM.4 makes no assertion about a
large core-free chamber.

### Dense isolated shell filling

An artificial dense filling can contain a large isolated region, but it need not obey
CM.1.  CM.1 uses the **contact-minimal global source**: if deleting a contact vertex
opened a strictly feasible insertion site, global optimality plus contact minimality
would permit a lower-contact representative.  This is the decisive information absent
from the regression.

### Heptagon plus center

The `n=8` minimizer with a contact-isolated center does not contradict CM.1: the unit
balls about the seven heptagon vertices cover the convex heptagon after deleting any
contact vertex only if that deleted vertex is nonisolated in the chosen contact-minimal
representative.  CM is finite and makes no claim that isolated points can always be
absorbed into the core.

### Strictness

CM.1 requires a proposed insertion point to be at distance **strictly greater** than
one from every retained source point.  A point at distance exactly one would create a
new contact and does not contradict contact minimality.  This strict/equality boundary
is essential and is preserved throughout the proof.

### Diameter

No claim is made that the replacement has diameter strictly below `D`.  Because it lies
inside `K`, its diameter is at most `D`; the definition of `D(n)` then forces equality.
That is enough for the contact-minimal contradiction.

---

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| deletion covering CM.1 | proved | one-point strict reinsertion inside `K` contradicts contact minimality |
| nonisolated core lies in `F` | audited/reproved | positive contact equilibrium + discrete maximum principle |
| deep exterior isolate covering CM.2 | proved | CM.1 plus core containment |
| boundary-layer estimate CM.3 | proved | Steiner + inner-parallel coarea |
| macroscopic chamber CM.4 | proved | PI perimeter deficit + full-source area saturation + CM.3 |
| quadratic local isolate population CM.3.3 | proved | unit-covering area count |
| chamber admits a positive-gain finite rearrangement | not proved | strict gaps have no quantitative floor or lattice phase |
| Level I | still open | finite internal rearrangement/high-surplus branch remain |

---

## 7. Exact remaining implication

A sufficient low-surplus closure is now the following finite statement.

> **CMR — isolated-chamber rearrangement.**  Let `R_j->infinity` and let `S_j` be
> finite planar point sets with mutual distances strictly greater than one such that
> their closed unit disks cover `B(0,R_j-1)` and `S_j subset B(0,R_j)`.  If each
> `S_j` occurs as the core-free chamber cut from a contact-minimal global source above,
> prove that for all sufficiently large `j` there is a same-cardinality local
> replacement, supported a distance `o(R_j)` from the chamber boundary, that creates
> enough free capacity to reinsert one deleted contact-core vertex; or derive an exact
> boundary/face surplus contradicting `b+Q<=2h`.
>
> A theorem for arbitrary strict packing-coverings would be stronger than necessary.
> The source-specific CM deletion-covering property may be used for every contact
> vertex and is the natural extra global-optimality input.

The key remaining scale problem is now explicit: prove an `o(D)` support bound from
strict packing plus unit covering and the global deletion-covering certificate, or
show that failure of such a bound forces the exact C-II face surplus.
