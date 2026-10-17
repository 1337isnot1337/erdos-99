> Generated reading edition · [exact source](../../../docs/reports/target_c_explicit_anti_reuleaux_kneser_poulsen_2026-09-09.md) · source SHA-256 `618c646c2a29418488bbaa609e716a49815976647564a2d5a32af68f7fe68751`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 16 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-01883B3CFD26","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — E43: an explicit anti-Reuleaux triple gap from planar Kneser–Poulsen

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-explicit-anti-reuleaux`  
**Base:** `cf790155660ad46797e53c7f44371b078f7eab7b`  
**Run type:** quantitative replacement for the compactness step in C43  
**Target:** global source geometry / Target C response inputs  
**Depends on:** canonical Oler inequality and strict global diameter upper bound; planar Kneser–Poulsen intersection theorem  
**Computation:** one fixed three-disk area interval evaluation  
**New external literature:** Bezdek–Connelly 2002

## LEVEL I STATUS

**STILL OPEN.**

Canonical C43 proves the existence of an absolute `eta_0>0` such that every triple in every sufficiently large global minimum-diameter configuration has one pair at distance at most `(1-eta_0)D`, but its compactness proof leaves `eta_0` unspecified.

Planar Kneser–Poulsen makes the container step quantitative.

### Theorem E43 — explicit anti-Reuleaux triple gap

For every sufficiently large global minimum-diameter unit-separated planar source `A` of diameter `D`, every three distinct source points `a,b,c` satisfy

```math
\boxed{
\min\{|a-b|,|b-c|,|c-a|\}
\le \frac{24}{25}D.
}
\tag{E43.1}
```

Thus canonical C43 may take

```math
\boxed{\eta_0=\frac1{25}=0.04,}
\qquad
\boxed{\rho_0=\frac{24}{25},}
\qquad
\boxed{\gamma_0=1-\rho_0^2=\frac{49}{625}=0.0784.}
\tag{E43.2}
```

The proof below also gives a conservative explicit scale: the contradiction already holds whenever `D>=274`. Using the canonical Oler lower bound on `D(n)`, for example `n>=69000` is more than sufficient to enter this scale. This numerical `n` threshold is not optimized and is not needed for the asymptotic theorem.

---

## 1. External theorem: planar Kneser–Poulsen for intersections

Bezdek and Connelly proved the planar Kneser–Poulsen conjecture:

> If a finite family of disks in the Euclidean plane is rearranged so that no pairwise distance between disk centers increases, then the area of their intersection does not decrease.

Equivalently, if one configuration of centers is a contraction of another, the contracted family has intersection area at least as large.

Source:

Károly Bezdek and Robert Connelly, *Pushing Disks Apart — The Kneser–Poulsen Conjecture in the Plane*, Journal für die reine und angewandte Mathematik **553** (2002), 221–236; arXiv:math/0108098.

The theorem applies directly to three congruent radius-`D` disks.

---

## 2. Triple-disk container

Suppose for contradiction that three source points satisfy

```math
|a-b|>\frac{24}{25}D,
\qquad
|b-c|>\frac{24}{25}D,
\qquad
|c-a|>\frac{24}{25}D.
\tag{2.1}
```

Every source point `x in A` lies within distance `D` of each of `a,b,c`, because `D=diam(A)`. Therefore

```math
\boxed{
A\subset K:=\overline B(a,D)\cap\overline B(b,D)\cap\overline B(c,D).
}
\tag{E43.3}
```

The set `K` is convex.

Scale by `D`. The three unit-disk centers then have all pairwise distances strictly greater than

```math
r:=\frac{24}{25}.
```

Move the three centers to an equilateral triangle of side exactly `r`. This is a contraction: every target pairwise distance `r` is no larger than the corresponding original pairwise distance.

By planar Kneser–Poulsen,

```math
\boxed{
area(K)
\le I(r)D^2,
}
\tag{E43.4}
```

where `I(r)` is the common-intersection area of three unit disks centered at the vertices of an equilateral triangle of side `r`.

---

## 3. Exact equilateral three-disk intersection area

Let

```math
h_r:=\sqrt{1-r^2/4},
```

```math
s_r:=\sqrt3\,h_r-r/2,
```

and

```math
\alpha_r:=2\arccos(r/2)-\frac\pi3.
```

The common intersection is a curvilinear equilateral triangle. Its three corner vertices form an equilateral triangle of side `s_r`; each of its three boundary arcs subtends angle `alpha_r` in a unit circle. Hence

```math
\boxed{
I(r)
=
\frac{\sqrt3}{4}s_r^2
+rac32\bigl(\alpha_r-\sin\alpha_r\bigr).
}
\tag{E43.5}
```

At `r=1`, this reduces to the standard unit Reuleaux-triangle area `(pi-sqrt3)/2`.

For the exact rational value

```math
r=\frac{24}{25},
```

we have

```math
h_r=\frac{\sqrt{481}}{25},
\qquad
s_r=\frac{\sqrt{1443}-12}{25},
```

```math
\alpha_r=2\arccos\frac{12}{25}-\frac\pi3.
```

Substitution in E43.5 gives

```math
\boxed{
I(24/25)
=0.7754263997509266927310266112\ldots .
}
\tag{E43.6}
```

A 50-decimal outward-rounded interval evaluation of the displayed exact expression gives

```math
0.77542639975092669273102661124479567
< I(24/25)
<0.77542639975092669273102661124479568.
```

Therefore

```math
\boxed{
\frac\pi4-I(24/25)
>0.0099717636465216.
}
\tag{E43.7}
```

Only the coarse strict inequality `I(24/25)<0.776<pi/4` is needed below.

---

## 4. Oler forces every global-minimum source container to have area `pi D^2/4-O(D)`

Apply the canonical finite Oler inequality to the `n` unit-separated source points inside the convex container `K`:

```math
n\le\frac{2}{\sqrt3}area(K)+\frac12 per(K)+1.
```

Equivalently,

```math
area(K)
\ge
\frac{\sqrt3}{2}(n-1)
-\frac{\sqrt3}{4}per(K).
\tag{4.1}
```

Because `K` is contained in the radius-`D` disk about `a`, perimeter monotonicity for planar convex bodies gives

```math
per(K)\le2\pi D.
\tag{4.2}
```

The canonical strict lattice-averaging upper bound for the global minimum diameter is

```math
D^2<\frac{2\sqrt3}{\pi}n.
```

Thus

```math
n>\frac{\pi}{2\sqrt3}D^2.
\tag{4.3}
```

Insert (4.2)–(4.3) into (4.1):

```math
\boxed{
area(K)
>
\frac\pi4D^2
-\frac{\sqrt3\pi}{2}D
-\frac{\sqrt3}{2}.
}
\tag{E43.8}
```

Hence

```math
\liminf_{D\to\infty}\frac{area(K)}{D^2}\ge\frac\pi4.
```

This is the quantitative version of the packing-area side of the original C43 compactness proof.

---

## 5. Contradiction and an explicit diameter scale

E43.4 and E43.6 give

```math
area(K)
\le
0.775426399750927D^2.
\tag{5.1}
```

E43.8 gives

```math
area(K)
>
0.785398163397448D^2
-2.72069904635133D
-0.866025403784439.
\tag{5.2}
```

The lower bound in (5.2) exceeds the upper bound in (5.1) as soon as

```math
D>273.1583\ldots .
```

Therefore the contradiction certainly holds for every

```math
\boxed{D\ge274.}
\tag{E43.9}
```

This proves E43.1 for all sufficiently large global minimizers.

Using the canonical Oler diameter lower bound

```math
D(n)\ge
\sqrt{\frac{2\sqrt3}{\pi}(n-1)+\frac34}
-\frac{\sqrt3}{2},
```

one checks that `n>=69000` implies `D(n)>274`. Thus `69000` is a conservative explicit cardinality threshold for E43.1, conditional only on the same canonical diameter inequalities used above.

---

## 6. Exact consequence for the response stack

Canonical C43 defines

```math
\rho_0=1-\eta_0,
\qquad
\gamma_0=1-\rho_0^2.
```

E43 gives the explicit choices

```math
\boxed{
\rho_0=24/25,
\qquad
\gamma_0=49/625.
}
\tag{E43.10}
```

Thus every sufficiently large C-II harmonic attachment clique contains a response pair of length at most

```math
\frac{24}{25}D,
```

and each unit of response conductance on such a pair contributes at least

```math
\boxed{
\frac{49}{625}D^2
}
```

to the C41 squared-diameter defect.

This turns every C43/C44 constant that was formerly existential into an explicit number. For example C44 may take

```math
K_0=\left\lceil\frac{9\pi}{24/25}\right\rceil=30.
```

The C44 Branch-A trace gap becomes

```math
\boxed{tr(\Lambda-L_H)\ge49/625=0.0784.}
```

No claim is made here that C44 itself is the shortest post-ZF route; the point is that its global geometric constant is now explicit.

---

## 7. How sharp is 24/25?

For an equilateral triple of normalized center side `r`, the exact intersection function E43.5 is strictly decreasing in `r` on the relevant range.

The scalar equation

```math
I(r)=\frac\pi4
```

has numerical root

```math
r_*=0.9544757052109578\ldots .
```

So the present Oler/Kneser–Poulsen argument can in principle take any fixed

```math
r>r_*,
\qquad
\eta_0<1-r_*=0.0455242947890\ldots,
```

with a sufficiently large threshold. The rational choice `r=24/25=0.96` leaves a comfortable area margin and simple exact constants.

The endpoint `r_*` itself cannot be used directly with this asymptotic argument because the quadratic area margin vanishes there.

---

## 8. Regression audit

### Direction of Kneser–Poulsen

The actual center triangle has all sides greater than `24D/25`; moving it to the equilateral `24D/25` triangle is a contraction. Intersection area can only increase under contraction, so the actual triple-disk intersection is bounded **above** by the equilateral one. The inequality direction is essential.

### No Reuleaux-shape assumption

The actual three centers need not form an equilateral or even acute triangle. Kneser–Poulsen is exactly what removes that shape dependence.

### Oler container perimeter

The triple-disk intersection may have diameter up to `2D`; the proof does not falsely use `per(K)<=pi D`. It uses only `K subset B(a,D)`, hence `per(K)<=2pi D`.

### Strict versus non-strict triple threshold

Assuming all three pair distances are `>24D/25` yields the contradiction. Therefore at least one pair is `<=24D/25`.

### Finite computation

The only numerical check is the fixed exact expression E43.5 at `r=24/25`; an outward-rounded interval is recorded. The theorem does not infer any asymptotic fact from a search or numerical experiment.

---

## 9. Literature audit

**Primary theorem used:**

K. Bezdek and R. Connelly, *Pushing Disks Apart — The Kneser–Poulsen Conjecture in the Plane*, J. Reine Angew. Math. 553 (2002), 221–236; arXiv:math/0108098.

The paper proves that when pairwise center distances of a finite planar disk family do not decrease, union area does not decrease and intersection area does not increase. Reversing the move gives the contraction formulation used here.

No higher-dimensional Kneser–Poulsen statement is used.

---

## 10. Classification

**Status:** proved report-level explicit strengthening of canonical C43, conditional on the cited planar Kneser–Poulsen theorem.  
**Level I:** still open.  
**New external literature:** Bezdek–Connelly 2002.  
**Explicit constants:** `eta_0=1/25`, `rho_0=24/25`, `gamma_0=49/625`; conservative `D>=274`, `n>=69000`.

## 11. Next exact target

Use the explicit anti-Reuleaux gap inside the FAQ/ANS equality neighborhood.

FAQ equality forces a diametral equilateral triple. E43 says every source triple has one pair at most `0.96D`. Therefore a Target C PI quadrilateral cannot lie arbitrarily close to FAQ equality.

The next finite optimization is:

> maximize the perimeter of a diameter-one quadrilateral with unit diagonals at angle `phi` when every vertex triple contains a pair of length at most `24/25`.

If this constrained maximum is quantitatively below FAQ's unconstrained `P_4(phi)`, insert it into the ANS nested-stability formula. This should produce a much larger explicit improvement above `0.4807218398...` than the current unconstrained FAQ bonus.

## 12. Compact handoff

```text
E43 explicit C43:
Assume a,b,c all have pairwise distance >rD with r=24/25. Every source point lies in
    K=B(a,D) cap B(b,D) cap B(c,D).
Contract the three disk centers to an equilateral triangle of side rD. Planar
Kneser-Poulsen says intersection area increases under contraction, hence
    area(K) <= I(r) D^2.
For three unit disks at equilateral center side r,
    I(r)=sqrt(3)s^2/4 + (3/2)(alpha-sin alpha),
    s=sqrt(3)*sqrt(1-r^2/4)-r/2,
    alpha=2 acos(r/2)-pi/3.
At r=24/25,
    I(r)=0.77542639975092669... < pi/4
by margin 0.00997176364652....

Oler on n source points inside K plus per(K)<=2pi D and the strict global upper
D^2<(2sqrt3/pi)n gives
    area(K) > pi D^2/4 - (sqrt3 pi/2)D - sqrt3/2.
Contradiction for D>=274. Thus every triple has a pair <=24D/25 for all sufficiently
large global minimizers. One may take
    eta_0=1/25, rho_0=24/25, gamma_0=49/625.
A conservative explicit n threshold from the canonical Oler diameter lower bound is
    n>=69000.
```
