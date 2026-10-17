> Generated reading edition · [exact source](../../research/target_c_support7_ground_sign_exact_classification_2026-09-19.md) · source SHA-256 `f47e1b8a60c7333147e6086d2b2dde573e526b36aeacd775056f3e58bc088a74`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9af5760ecb130a8d13dc9af044ffeb3cb390d894", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_ground_sign_exact_classification_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0bfd3c002360fa10263be5db9d524219956765a4c5a256d6418a5ccbc9b2e15c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - exact ground-only sign classification at support seven

**Date:** 2026-09-19  
**Status:** exact local feasibility classification; theorem-state authority unchanged  
**Scope:** seven strictly ordered signed unit ground rays; first in an open semicircle, then under the support-seven `H6` width bound `<2pi/3`  
**Certificate:** `research/verify_target_c_support7_ground_sign_exact_classification_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding ground-projection reduction proved that fourteen of the `35` possible `3+4` sign patterns are impossible whenever the seven raw ground rays lie in an open semicircle, and that eight additional patterns are impossible in `H6` because its ground cone has width `<2pi/3`.

This note closes the converse direction at exactly that local level. Every pattern not excluded by those arguments has an exact strict signed-unit-vector realization in the stated angular regime.

Consequently the previous ground-only exclusions are complete: there is no stronger conclusion available from the seven ground rays using only their linear order, the cone-width bound, unit lengths, and signed equilibrium.

## 1. Open-semicircle classification

Let

```math
\theta_1<\theta_2<\cdots<\theta_7<\theta_1+\pi,
\qquad
u_i=(\cos\theta_i,\sin\theta_i),
```

and let `P` be the size-three sign class. The ground equilibrium is

```math
\sum_{i\in P}u_i=\sum_{i\notin P}u_i.
\tag{1.1}
```

The previously certified pivot/matching obstruction excludes exactly

```text
123 124 125 127 134 135 137 157 167 357 367 457 467 567
```

among the `35` possible choices of `P`.

The exact constructive certificate in this note realizes every one of the remaining `21` patterns:

```text
126 136 145 146 147 156 234 235 236 237 245
246 247 256 257 267 345 346 347 356 456
```

Therefore

```math
\boxed{
\text{open semicircle: exactly }21/35\text{ ground }3+4\text{ sign patterns are realizable.}
}
\tag{1.2}
```

Equivalently, the fourteen pivot/matching exclusions are the complete ground-only order classification for an arbitrary open semicircle.

## 2. Exact `H6` width classification

At the support-seven `H6` endpoint the ground hull cone satisfies

```math
\theta_7-\theta_1<\frac{2\pi}{3}.
\tag{2.1}
```

The previously certified bisector/layer-cake argument excludes eighteen patterns, ten of which overlap the fourteen open-semicircle exclusions. Its eight new exclusions are

```text
126 136 146 147 246 247 257 267
```

so the union excludes `22/35` patterns.

The certificate below gives an exact strict width-`<2pi/3` realization for every remaining pattern:

```text
145 156 234 235 236 237 245 256 345 346 347 356 456
```

Hence

```math
\boxed{
H6:\quad
P\in\{145,156,234,235,236,237,245,256,345,346,347,356,456\}
}
\tag{2.2}
```

is an if-and-only-if classification at the ground-only level.

In particular,

```math
\boxed{
\text{H6 ground-only feasibility has exactly }13/35\text{ sign patterns.}
}
\tag{2.3}
```

## 3. Exact constructive witness scheme

The realizability proof uses the rational half-angle parameterization

```math
u(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),
\qquad t\in\mathbb Q,
\tag{3.1}
```

whose canonical angle is `2 arctan(t)` in `(-pi,pi)`.

For each surviving pattern, choose two positions `a<b` carrying the same sign and assign rational half-angle parameters to the other five rays. Write `s_i=+1` on the minority class and `s_i=-1` on its complement, and let

```math
\sigma=s_a=s_b.
```

The two missing unit vectors must have sum

```math
R=-\frac1\sigma\sum_{i\ne a,b}s_i u(t_i).
\tag{3.2}
```

The committed witness data are chosen so that

```math
0<r^2:=|R|^2<4.
```

Put

```math
q=\frac{4-r^2}{r^2}>0
```

and let `J(x,y)=(-y,x)`. Then

```math
\boxed{
 u_a=\frac R2+\frac{\sqrt q}{2}JR,
\qquad
 u_b=\frac R2-\frac{\sqrt q}{2}JR.
}
\tag{3.3}
```

Since `JR` is perpendicular to `R`,

```math
|u_a|^2=|u_b|^2
=\frac{r^2}{4}(1+q)=1,
```

and `u_a+u_b=R`. Thus (3.2) gives the signed equilibrium (1.1) exactly.

Every witness lies in a quadratic extension `Q(sqrt(q))`. The verifier implements exact sign comparison in that field, so none of the strict-order or cone-width checks uses floating point.

## 4. What the verifier checks

For all `35` patterns, the certificate independently recomputes the two existing impossibility mechanisms and locks their exact finite sets:

- `14` open-semicircle pairing exclusions;
- `18` H6 bisector exclusions;
- overlap `10`;
- union `22`.

It then checks all `21` constructive witnesses. For each witness it proves exactly that:

1. all seven vectors have unit norm;
2. the signed vector sum is zero;
3. the canonical half-angle coordinates are strictly increasing, hence `theta_1<...<theta_7`;
4. the endpoint cross product is positive, hence the total width lies strictly in `(0,pi)`;
5. for the thirteen H6 witnesses, the endpoint dot product is greater than `-1/2`, hence the width is `<2pi/3`;
6. for the extra eight open-semicircle witnesses, the endpoint dot product is less than `-1/2`, so these chosen examples genuinely lie outside the H6 width regime.

The final census is therefore exact, not numerical evidence.

## 5. Consequence for the remaining `H6` branch

This result does **not** realize a full support-seven reciprocal `H6` configuration. It realizes only the seven signed unit rays at the ground vertex.

Its use is to close a search direction. Every one of the thirteen patterns left by the previous H6 projection proof is genuinely feasible at the ground under all ground-only hypotheses currently available. Therefore no additional argument that depends only on

- the seven ground-ray directions,
- their strict linear order,
- unit magnitudes,
- the `3+4` sign split,
- signed ground equilibrium, and
- the cone-width bound `<2pi/3`

can eliminate any of those thirteen patterns.

Any further `H6` reduction must couple the ground to non-ground data. The next finite layer should impose the actual relation graph (`C7` or `C3+C4`) and the cyclic positions of relation-edge signs at the five non-ground hull pentagons, then intersect that with the exact pentagon gap-order/closure theorem and the reciprocal collinearity restrictions.

No theorem-state file is changed. C-II remains open.
