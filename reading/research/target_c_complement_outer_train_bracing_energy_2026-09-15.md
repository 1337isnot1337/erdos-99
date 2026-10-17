> Generated reading edition · [exact source](../../research/target_c_complement_outer_train_bracing_energy_2026-09-15.md) · source SHA-256 `d14fcf3f86c824dbdcc613165fdc3cf0eb3a4b8ffae7ffdf9f5ede8ca8cf59a0`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 24 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ff3b3e1772de603b8a7a3259a8ec964fe04a24a6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_complement_outer_train_bracing_energy_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "bdc6d20ad27c37c86075db045bd251c97d60d271fe4a93a5dbf0d41bf7b2a6d3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — complement outer-train bracing adds a second energy payment

**Date:** 2026-09-15  
**Status:** proof-only low-`t` Type-II strengthening; theorem-state authority unchanged  
**Scope:** full-core/no-container Type-II branch  
**Dependencies:** audited §§142, 157 and Type-II near-disk geometry; dominant-orbit outer-energy and joint capacity/energy refinements  
**LEVEL I STATUS:** `STILL OPEN`

The dominant-orbit argument leaves a very rigid escape at its scalar endpoint.  Almost
all trains outside the dominant atomic `pi/3` orbit must use **both** of their terminal
incidences on the outer face.  Those complement outer-to-outer trains were not used in
the first energy theorem.

Audited §157 now supplies the missing geometry: every outer-to-outer train is crossed
by actual diameter edges with both transverse signs.  In the Type-II near-disk limit,
that forces the train direction to pass through the normal-angle interval of either
outer shore.  Consequently a train whose two outer terminals are not nearly antipodal
pays a definite amount of terminal directional energy.

There is also a global packing constraint.  Partition train phases into three
half-open projective sectors of width `pi/3`.  Two trains in one sector cannot cross,
because a strict-rhombus train crossing requires projective direction separation
strictly greater than `pi/3`.  A noncrossing family cannot contain too many nearly
antipodal outer pairs: its endpoint intervals must nest, and the round-hull perimeter
measure limits the endpoint density.

Combining this second, disjoint energy payment with the retained dominant-orbit energy
raises the safe proof-only low-`t` floor to

```math
\boxed{
\liminf {q-k\over D}\ge1.82806.
}
```

The numerical scalar crossing is approximately `1.8280659`; the theorem uses the
round value `1.82806`.

---

## 1. Dominant and complement train populations

Retain

```math
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
```

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
C_0=2\sqrt{\Delta_2}+0.00042,
```

and

```math
U={9t\over2}-2\pi-2\delta-{\kappa\over2}.
```

The low-`t` envelope is

```math
C_0\le C={T-q/2\over D}\le U,
\tag{BE.1}
```

so

```math
2\delta+{\kappa\over2}
\le R(t):={9t\over2}-2\pi-C_0.
\tag{BE.2}
```

Freeze shrinking phase windows around one dominant atomic orbit.  Let

- `M` be its absolute train mass per `D`;
- `K` be the number of its outer terminal occurrences per `D`;
- `N_c` be the number of complete trains outside those windows per `D`.

The orbit/Mantel argument gives

```math
M\ge{4\Delta_2\over C}.
```

Since

```math
{T\over D}=C+{t+\kappa\over2},
```

and the function `C-4Delta2/C` is increasing,

```math
\boxed{
N_c
\le N_*:=
U+{t+\kappa\over2}-{4\Delta_2\over U}.
}
\tag{BE.3}
```

---

## 2. Joint orbit energy also gives an upper bound on `K`

The joint capacity/energy theorem applies to the **actual** dominant-window outer
occurrence population, before any lower bound on that population is inserted.  It gives

```math
\delta\ge\Phi(K),
\tag{BE.4}
```

where

```math
\Phi(z)=z-6\arcsin(\tanh(z/6))
```

on the present range.  Since `Phi` is increasing, define

```math
Q(\delta):=\Phi^{-1}(\delta).
```

Then

```math
\boxed{K\le Q(\delta).}
\tag{BE.5}
```

The total outer occurrence density is `pi+delta`.  Hence complement trains carry at
least

```math
\pi+\delta-Q(\delta)
```

outer terminal occurrences per `D`.

If `P_c` is the number of complement trains with **two** outer terminal occurrences,
then a complement train not counted by `P_c` contributes at most one outer occurrence.
Therefore

```math
\pi+\delta-Q(\delta)
\le N_c+P_c.
```

Using (BE.3),

```math
\boxed{
P_c
\ge P_*:=
\pi+\delta-Q(\delta)-N_*.
}
\tag{BE.6}
```

At the previous orbit-energy endpoint this lower bound is essentially the whole
complement train population: exposed-hull equality is being approached from both
sides.

---

## 3. Retain complement pairs under round-hull perimeter capacity

Consider only the `P_cD+o(D)` complement outer-to-outer trains.  On loaded-hull route
`W_i`, let `c_i` be the number of terminal occurrences of these trains.  Since every
such occurrence is an outer edge occurrence,

```math
c_i\le\ell_i=s_i+d_i,
```

where `s_i` is the loaded-hull side length and `d_i=ell_i-s_i` its route detour.

Assign fractional weights in `[0,1]` to these endpoint occurrences so that the retained
endpoint weight on route `i` is at most `s_i`.  The total endpoint weight discarded on
that route need be no more than

```math
(c_i-s_i)_+\le d_i.
```

For a train with endpoint weights `a_tau,b_tau`, retain the pair with weight

```math
w_\tau=\min(a_\tau,b_\tau).
```

Then

```math
1-w_\tau
\le(1-a_\tau)+(1-b_\tau).
```

Summing over all complement two-outer trains and using

```math
\sum_i d_i=d_{out},
```

shows that the retained **pair** mass is at least

```math
\boxed{
p
\ge P_c-\delta.
}
\tag{BE.7}
```

Combining with (BE.6),

```math
\boxed{
p\ge p_*:=
\pi-Q(\delta)-N_*.
}
\tag{BE.8}
```

The `+delta` in the outer occurrence count and the at-most-`delta` endpoint-capacity
loss cancel exactly.

The two weighted endpoint measures are dominated by the physical loaded-hull perimeter
measure.  Type-II near-disk geometry makes that measure converge, in oriented normal
angle `theta in R/2pi Z`, to

```math
{1\over2}\,d\theta.
\tag{BE.9}
```

The factor `1/2` is the circle-radius normalization: a diameter-`D` disk has radius
`D/2` and perimeter `pi D`.

---

## 4. Two-sided diameter bracing forces a terminal-energy cost

Take one outer-to-outer train `tau` with projective contact direction `u`.  Its train
midpoint arc gives a Jordan shore split.  Choose the shore whose corresponding loaded
hull normal-angle arc has smaller width

```math
0\le w_\tau\le\pi.
```

Audited §157 says that actual diameter edges crossing this train occur with both signs
of

```math
r_h\cdot Ju.
\tag{BE.10}
```

In the Type-II near-disk limit, every diameter vector oriented into the chosen shore is
`D-o(D)` in the radial outward-normal direction of its loaded endpoint.  Uniformly over
actual diameter pairs,

```math
{r_h\over D}=n_h+o(1),
\tag{BE.11}
```

where `n_h` is that endpoint's circular normal direction.

Hence the normal-angle interval of the chosen shore contains directions on both sides
of a zero of `n dot Ju`.  Equivalently, up to `o(1)`, one representative of the train
phase lies inside the normal-angle interval between the two outer terminal locations.

Put that interval at `[0,w]` and let the train phase representative be `phi in[0,w]`.
The loaded-hull tangents at the two ends have projective directions `pi/2` and
`w+pi/2`.  The two terminal edge occurrences themselves have train phase `phi`.
Their exact route directional energies are bounded below by the projective energies,
so their sum is at least

```math
\begin{aligned}
&[1-|\cos(\phi-\pi/2)|]
+[1-|\cos(\phi-w-\pi/2)|]\\
&=2-\sin\phi-\sin(w-\phi)\\
&\ge2-2\sin(w/2).
\end{aligned}
```

Thus every outer-to-outer train obeys the asymptotic terminal-energy floor

```math
\boxed{
E_{term}(\tau)
\ge B(w_\tau)-o(1),
\qquad
B(w):=2-2\sin(w/2).
}
\tag{BE.12}
```

Writing the antipodal deficit

```math
r_\tau:=\pi-w_\tau,
```

this is

```math
\boxed{
B(w_\tau)=2-2\cos(r_\tau/2).
}
\tag{BE.13}
```

So low terminal energy is possible only when the two outer ends are nearly antipodal.

---

## 5. Phase sectors make three noncrossing families

Partition the projective train-phase circle into three half-open sectors of width
`pi/3`.  Audited §142 proves that two complete trains can cross only when their
projective contact directions differ by **strictly more** than `pi/3`.  Therefore
trains in one sector do not cross.

The convex-pocket augmentation from Sections 67/126 lets each outer terminal occurrence
be pushed to the corresponding loaded-hull boundary position through disjoint pockets,
preserving cyclic order.  A noncrossing train midpoint family therefore gives a
noncrossing chord family on the convex boundary.

We now need one finite/measure lemma for such a family.

### Lemma BE.1 — near-antipodal capacity in one noncrossing family

Let a weighted pairwise-noncrossing chord family have endpoint measures dominated by
`(1/2)dtheta` on a circle.  For each chord let

```math
r=\pi-w
```

be its antipodal deficit, where `w<=pi` is the smaller endpoint angular separation.
For every

```math
0<r_0<\pi/3,
```

the total chord weight with `r<=r_0` is at most

```math
\boxed{r_0/2.}
\tag{BE.14}
```

#### Proof

Every chord counted in (BE.14) has shorter boundary arc length at least

```math
\pi-r_0>{2\pi\over3}.
```

Because the chords do not cross, these shorter arcs form a laminar family.  There are
at most two top-level disjoint arcs: three disjoint arcs of length greater than
`2pi/3` cannot fit on a circle of length `2pi`.

Inside one top-level arc the relevant shorter arcs form a single nested chain.  Two
disjoint children would each have length greater than `2pi/3`, while the parent has
length at most `pi`, impossible.

For one nested chain, cut just outside its top-level arc and write the left endpoints
in increasing order and right endpoints in decreasing order.  Let `A` and `B` be the
angular spans of the left- and right-endpoint sets.  The outermost and innermost chord
lengths both lie in `[pi-r_0,pi]`, and their difference is exactly `A+B`.  Hence

```math
A+B\le r_0.
\tag{BE.15}
```

If the chain has total weight `m`, domination of each endpoint measure by
`(1/2)dtheta` gives

```math
2m\le A,
\qquad
2m\le B.
```

Therefore

```math
4m\le A+B\le r_0,
\qquad
m\le r_0/4.
```

There are at most two top-level chains, proving total weight at most `r_0/2`.  The
finite-source version carries an `o(1)` discrepancy from the near-disk perimeter
measure; it vanishes in the limit.  QED.

---

## 6. Energy of one noncrossing family

Let one sector family have retained pair mass `m<=pi/6`.  Lemma BE.1 says that the
quantile of the antipodal deficit satisfies

```math
r(s)\ge2s,
\qquad0\le s\le m.
```

Since the cost in (BE.13) is increasing in `r`,

```math
\begin{aligned}
E_{sector}
&\ge\int_0^m[2-2\cos(r(s)/2)]\,ds\\
&\ge\int_0^m[2-2\cos s]\,ds.
\end{aligned}
```

Thus

```math
\boxed{
E_{sector}
\ge E(m):=2m-2\sin m,
\qquad 0\le m\le\pi/6.
}
\tag{BE.16}
```

If a sector mass exceeds `pi/6`, retain only weight `pi/6`; then

```math
E_{sector}\ge E(\pi/6)=\pi/3-1>0.047.
\tag{BE.17}
```

For total retained complement pair mass `0<=p<=1`, the latter value already exceeds
the final three-sector bound below.  Otherwise all three sector masses are at most
`pi/6`, and convexity of `E` plus Jensen gives

```math
\sum_{j=1}^3E(m_j)
\ge3E(p/3).
```

Therefore every retained complement family of total pair mass `p<=1` pays

```math
\boxed{
E_{comp}
\ge J(p):=2p-6\sin(p/3).
}
\tag{BE.18}
```

The cost is cubic at the origin:

```math
J(p)={p^3\over27}+O(p^5).
```

---

## 7. Add the dominant and complement payments without overlap

The first dominant-orbit theorem gives an **additive edge-energy** lower bound after
retaining only dominant-window outer occurrences up to hull-side length capacity.  Its
retained mass is at least

```math
z_*:=
\pi-t-\kappa-2U+{8\Delta_2\over U},
\tag{BE.19}
```

and the corresponding weighted dominant edge occurrences pay

```math
\boxed{
E_{dom}
\ge F(z_*),
\qquad
F(z)=z-6\sin(z/6).
}
\tag{BE.20}
```

The complement terminal edge occurrences in Sections 3--6 belong to trains outside the
dominant windows.  They are therefore disjoint from the edge occurrences used in
(BE.20).  Their energy payments can be added.

Using (BE.8), define

```math
\boxed{
p_*:=
\left[
\pi-Q(\delta)-
U-{t+\kappa\over2}+{4\Delta_2\over U}
\right]_+.
}
\tag{BE.21}
```

On the low-`t` interval considered below, `p_*<1`.  The total outer detour must satisfy

```math
\boxed{
\delta
\ge
F(z_*)+J(p_*).
}
\tag{BE.22}
```

This is the new coupled scalar obstruction.

---

## 8. The feasible triangle is again minimized at maximum detour and `kappa=0`

Define the contradiction margin

```math
\mathcal M(t,\delta,\kappa)
:=F(z_*)+J(p_*)-\delta.
```

On the interval

```math
t_{42}\le t\le1.82806,
```

the following uniform bounds hold (certified by the companion script):

```math
0<z_*<1.33,
\qquad
0.61<p_*<1,
\qquad
Q(\delta)<1.62.
\tag{BE.23}
```

### `kappa` direction

At fixed `t,delta`,

```math
{\partial z_*\over\partial\kappa}
={4\Delta_2\over U^2}>0.
```

Also

```math
N_*:=U+{t+\kappa\over2}-{4\Delta_2\over U}
```

satisfies

```math
{\partial N_*\over\partial\kappa}
=-{2\Delta_2\over U^2}<0,
```

so `p_*` increases with `kappa`.  Since both `F` and `J` are increasing,

```math
\boxed{\mathcal M\text{ is minimized at }\kappa=0.}
\tag{BE.24}
```

### `delta` direction

At fixed `t,kappa`,

```math
{\partial z_*\over\partial\delta}
=4+{16\Delta_2\over U^2}<8.
```

For `z_*<1.33`,

```math
F'(z_*)=1-\cos(z_*/6)<0.025,
```

so the dominant term grows at rate less than `0.2`.

Since `Q=Phi^{-1}`,

```math
Q'(\delta)={1\over\Phi'(Q)}.
```

For `Q<1.62`,

```math
\Phi'(Q)<0.04,
\qquad
Q'(\delta)>25.
```

Moreover

```math
-{\partial N_*\over\partial\delta}
=2\left(1+{4\Delta_2\over U^2}\right)<4.
```

Hence

```math
{\partial p_*\over\partial\delta}<-21.
\tag{BE.25}
```

For `p_*>0.61`,

```math
J'(p_*)=2-2\cos(p_*/3)>0.041.
```

Therefore

```math
{\partial\mathcal M\over\partial\delta}
<0.2-21(0.041)-1<0.
\tag{BE.26}
```

Thus the margin decreases with detour.  The weakest feasible point is

```math
\boxed{
\kappa=0,
\qquad
\delta={R(t)\over2},
\qquad
U=C_0.
}
\tag{BE.27}
```

---

## 9. One-variable endpoint and new floor

At (BE.27), define

```math
\delta_0(t)={R(t)\over2},
```

```math
z_0(t)=
\pi-t-2C_0+{8\Delta_2\over C_0},
\tag{BE.28}
```

```math
N_0(t)=
C_0+{t\over2}-{4\Delta_2\over C_0},
\tag{BE.29}
```

and

```math
p_0(t)=
\pi-Q(\delta_0(t))-N_0(t).
\tag{BE.30}
```

The boundary margin is

```math
\boxed{
\mathcal M_0(t)
=F(z_0(t))+J(p_0(t))-\delta_0(t).
}
\tag{BE.31}
```

It is strictly decreasing on the displayed interval: `z_0'(t)=-1`,
`delta_0'(t)=9/4`, and

```math
p_0'(t)
=-{9/4\over\Phi'(Q(\delta_0(t)))}-{1\over2}<0.
```

At the safe round value

```math
t=1.82806,
```

the certificate gives

```math
\begin{aligned}
\delta_0&=0.019019539546249\ldots,\\
z_0&=1.311852838782208\ldots,\\
F(z_0)&=0.010427098810355\ldots,\\
p_0&=0.61559430013147\ldots,\\
J(p_0)&=0.00862195266439\ldots,
\end{aligned}
```

and therefore

```math
\boxed{
\mathcal M_0(1.82806)
=2.95119\times10^{-5}>0.
}
\tag{BE.32}
```

The numerical zero is approximately

```math
1.8280659\ldots .
```

Thus:

### Theorem BE.2 — complement outer-train bracing floor

Every full-core Type-II survivor sequence in the stated proof-only scope satisfies

```math
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge1.82806.
}
\tag{BE.33}
```

This supersedes the `1.82434` scalar floor from the joint dominant-orbit theorem.

---

## 10. Frontier effect

The improvement is not another decimal optimization of the same scalar.  It uses a
new independent physical resource:

```text
quadratic rhombus crossings
 -> one dominant atomic train orbit
 -> dominant orbit consumes outer directional energy

exposed-hull near equality
 -> many trains outside that orbit must be outer-to-outer
 -> Section 157 gives two-sided actual-diameter bracing
 -> low terminal energy forces near-antipodal endpoints
 -> three phase sectors are noncrossing
 -> near-antipodal endpoint pairs have only linear round-hull capacity
 -> complement trains consume a second, disjoint energy budget.
```

At the new endpoint the complement retained-pair floor is still about `0.615D`, so the
new mechanism is not being driven by a vanishing population.

C-II remains open.  Past `t≈1.828066`, the growing allowable detour weakens the forced
complement two-outer population quickly.  The next useful target is to avoid bounding
dominant-orbit outer occurrences only by the scalar inverse `Phi^{-1}(delta)`: use the
actual cyclic pairing of dominant and complement terminals, or inject the Woodall
near-extremal diameter topology into the noncrossing near-antipodal stacks.

## 11. Reproducibility

Run

```bash
python3 research/verify_target_c_complement_outer_train_bracing_energy.py
```

for the endpoint constants and derivative bounds.
