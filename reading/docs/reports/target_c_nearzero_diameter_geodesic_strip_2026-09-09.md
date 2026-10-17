> Generated reading edition · [exact source](../../../docs/reports/target_c_nearzero_diameter_geodesic_strip_2026-09-09.md) · source SHA-256 `f5a55c4e65f9c435f7ae6078a25fb322b1b169c564aca4b6c470c567583744f7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-1486B56B766D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — DGS: an almost-length-D contact geodesic between diameter endpoints is an o(D)-width source-interior strip

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** elementary polygonal-chain stability / source-hull localization  
**Target:** Target C near-zero carrier, interface with Target B C100--C102  
**Depends on:** NSE for the application; canonical Target A source-hull annulus (Section 155) for source-interiority  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

NSE proves that in the phase `D epsilon ->0`, the contact distance from the C66 star center `z` to its actual diameter-partner set is

```math
L=D+o(D).
```

Choose an actual diameter partner `a` with

```math
|a-z|=D,
\qquad
d_C(z,a)=L,
```

and a shortest unit-contact path

```math
z=x_0,x_1,\ldots,x_L=a.
```

Write

```math
u:=\frac{a-z}{D},
\qquad e_i:=x_i-x_{i-1},
\qquad |e_i|=1,
```

and define the path-length excess

```math
E:=L-D\ge0.
```

Then the path has the exact projection-defect identity

```math
\boxed{
\sum_{i=1}^L(1-e_i\cdot u)=E,
}
\tag{DGS.1}
```

and the transverse square bound

```math
\boxed{
\sum_{i=1}^L(e_i\cdot Ju)^2\le2E.
}
\tag{DGS.2}
```

Consequently every path vertex lies within distance

```math
\boxed{
B:=\sqrt{2LE}
}
\tag{DGS.3}
```

of the diameter segment line `za`.

In particular, if `E=o(D)`, then

```math
\boxed{B=o(D).}
\tag{DGS.4}
```

This requires no uniform cone assumption on the individual path edges.

Combining DGS with the canonical global-minimizer source-hull annulus

```math
B(o,D/2-2h)\subseteq K:=\operatorname{conv}A
\subseteq B(o,D/2+h),
\qquad
h=3^{1/4}\sqrt D,
\tag{DGS.5}
```

gives a direct source-interiority theorem:

### Theorem DGS — almost all geodesic vertices are source-hull interior

For all sufficiently large `D`, every path vertex satisfying

```math
\boxed{
\min\{j,L-j\}
>
E+3B+9h
}
\tag{DGS.6}
```

lies strictly inside `K`.

Hence when `E=o(D)`, all but

```math
\boxed{o(D)}
\tag{DGS.7}
```

vertices of the diameter geodesic are strict source-hull interior points and therefore cannot be endpoints of any diameter pair.

This recovers the useful source-interiority conclusion of the conditional C100 near-chain route directly from NSE, without assuming C100's stronger uniform edge-cone hypothesis.

It does **not** force contact-disk interiority or degree four. The exact degree-three and degree-five local regressions in `target_c_nearchain_interior_and_vertex_defects_2026-09-09.md` remain valid.

---

## 1. Exact longitudinal deficit

Because the path displacement is the diameter vector,

```math
\sum_{i=1}^Le_i
=a-z
=Du.
```

Taking the scalar product with `u`,

```math
\sum_i e_i\cdot u=D.
```

Since the path has `L` unit edges,

```math
\sum_i(1-e_i\cdot u)
=L-D
=E,
```

which proves DGS.1.

Every summand is nonnegative because `e_i dot u<=1`.

---

## 2. Transverse energy and strip width

Put

```math
s_i:=e_i\cdot u,
\qquad
t_i:=e_i\cdot Ju.
```

Since `|e_i|=1`,

```math
t_i^2=1-s_i^2=(1-s_i)(1+s_i)\le2(1-s_i).
```

Summing and using DGS.1 gives DGS.2:

```math
\sum_i t_i^2\le2E.
```

For the `j`th prefix, its transverse displacement is

```math
y_j:=\sum_{i=1}^jt_i.
```

Cauchy gives

```math
|y_j|^2
\le j\sum_{i=1}^jt_i^2
\le2LE.
```

Thus

```math
|y_j|\le B:=\sqrt{2LE}
```

for every `j`, proving DGS.3.

If `L=D+o(D)`, then `L=O(D)` and `E=o(D)`, so

```math
B/D\le\sqrt{2LE/D^2}=o(1),
```

which is DGS.4.

---

## 3. Prefix projections remain deep in the diameter segment

Write

```math
x_j=z+p_ju+y_jJu,
\qquad
p_j:=\sum_{i=1}^js_i.
```

Let

```math
E_j:=\sum_{i=1}^j(1-s_i).
```

Then

```math
p_j=j-E_j\ge j-E.
\tag{3.1}
```

For the suffix,

```math
D-p_j
=(L-j)-(E-E_j)
\ge L-j-E.
\tag{3.2}
```

Therefore

```math
\boxed{
\min\{p_j,D-p_j\}
\ge
\min\{j,L-j\}-E.
}
\tag{DGS.8}
```

In particular, if the right side is positive, then `0<p_j<D`.

---

## 4. Source-hull inward depth from the diameter chord

Let

```math
R:=D/2+h.
```

The source-hull annulus gives

```math
|z-o|\le R,
\qquad
|a-o|\le R.
```

For `0<=p<=D`, set

```math
w=z+pu
=(1-p/D)z+(p/D)a.
```

The exact convex-combination norm identity gives

```math
|w-o|^2
\le
R^2-p(D-p).
\tag{4.1}
```

Since `p(D-p)<=D^2/4<=R^2`,

```math
\sqrt{R^2-p(D-p)}
\le
R-\frac{p(D-p)}{2R}.
\tag{4.2}
```

Apply this to `p=p_j` and use `|y_j|<=B`:

```math
|x_j-o|
\le
R-\frac{p_j(D-p_j)}{2R}+B.
\tag{4.3}
```

Put

```math
m_j:=\min\{p_j,D-p_j\}.
```

When `m_j<=D/2`,

```math
p_j(D-p_j)
\ge m_j(D-m_j)
\ge\frac D2m_j.
```

For sufficiently large `D`, `h<D/4`, so

```math
R<D/2+D/4=3D/4,
```

and therefore

```math
\frac{p_j(D-p_j)}{2R}
>\frac{m_j}{3}.
\tag{4.4}
```

Thus

```math
|x_j-o|<R-\frac{m_j}{3}+B.
\tag{4.5}
```

The inner source-hull disk has radius

```math
D/2-2h=R-3h.
```

So `x_j` lies strictly inside that disk whenever

```math
\frac{m_j}{3}>B+3h,
```

i.e. whenever

```math
m_j>3B+9h.
```

By DGS.8, the sufficient condition is exactly DGS.6.

---

## 5. Count the exceptional path vertices

Only vertices within

```math
E+3B+9h
```

indices of one of the two path endpoints can fail DGS.6. Therefore the number of exceptional vertices is at most

```math
2(E+3B+9h)+O(1).
\tag{5.1}
```

Under NSE,

```math
E=o(D),
\qquad
B=o(D),
\qquad
h=O(\sqrt D)=o(D).
```

Hence (5.1) is `o(D)`, proving DGS.7.

An interior point of a diameter-`D` convex body cannot itself be a diameter endpoint: extending the ray from the opposite endpoint slightly beyond the interior point remains in the body and creates a distance greater than `D`. Thus every DGS-interior path vertex has no diameter reaction.

---

## 6. Interaction with S1E and Target B

At the S1E slope-one endpoint, the entire `1-o(1)` response mass and `D^2-o(D^2)` contact-stress mass lie in one harmonic component `I_*`. NSE chooses an actual diameter partner `a` whose shortest contact path from `z` has length `D+o(D)`. DGS therefore produces inside `I_*` an explicit diameter geodesic with:

```math
\text{path length}=D+o(D),
```

```math
\text{transverse width}=o(D),
```

and

```math
D-o(D)
```

source-hull-interior path vertices.

This supplies the geometric near-chain input that was previously conditional in C100, but only in the near-zero response phase.

The remaining C100--C102 obstruction is unchanged: source-hull interiority does not imply contact-disk interiority, and local degree-three/five rhombic patches can have arbitrarily small path turn while supporting positive equilibrium.

---

## 7. Regression audit

- DGS uses a shortest **contact** path whose endpoints are an actual diameter pair. An arbitrary near-geodesic path does not get DGS.1 unless its endpoint displacement is exactly `D`.
- Individual path edges may turn by a large angle. DGS controls only total projection deficit and global transverse width.
- `B=o(D)` is not `O(sqrt D)` without a rate on `E`; no stronger claim is made.
- The path strip does not contain the entire harmonic component.
- The degree-three and degree-five local regressions from the existing near-chain audit survive.

## 8. Next target

The new cross-route endpoint is now precise:

1. S1E/NSE: one harmonic component carries almost all stress/response and has graph diameter `D+o(D)`;
2. DGS: it contains an actual diameter contact geodesic in an `o(D)` strip, with all but `o(D)` path vertices source-hull interior;
3. S1E: the component has Eppstein slack `o(D)`;
4. C42: if the force-visible population is quadratic, all but `O(D)` face incidences are strict rhombi.

The next theorem should use **Eppstein near-equality plus the DGS diameter geodesic** to control vertices away from that geodesic. A sufficient statement is that a triangle-free penny graph with Eppstein slack `o(D)` and an exact diameter geodesic of transverse width `o(D)` has only `o(D^2)` vertices unless a positive-density strict-rhombic strip crosses the geodesic. That latter alternative is the natural entry point for Target B train/phase arguments.

## 9. Compact handoff

```text
DGS removes C100's uniform-edge-cone assumption in the NSE phase.
Take a shortest contact path z=x_0,...,x_L=a with |a-z|=D and L=D+E.
For u=(a-z)/D and unit edge vectors e_i:
    sum(1-e_i dot u)=E,
    sum(e_i dot Ju)^2<=2E.
Hence every path vertex has transverse displacement <=B=sqrt(2LE).
If E=o(D), then B=o(D).

Using the canonical source-hull annulus
    B(o,D/2-2h) subset K subset B(o,D/2+h), h=3^(1/4)sqrt(D),
all vertices with
    min(j,L-j)>E+3B+9h
lie strictly inside K. Thus all but o(D) path vertices are source-hull interior and
cannot be diameter endpoints.

At S1E, this produces a D+o(D) diameter geodesic in an o(D)-width strip inside the unique
D^2-stress carrier. The remaining obstacle is contact-disk degree/face structure, not
source-hull localization.
```
