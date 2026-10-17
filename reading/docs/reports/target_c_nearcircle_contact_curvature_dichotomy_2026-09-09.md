> Generated reading edition · [exact source](../../../docs/reports/target_c_nearcircle_contact_curvature_dichotomy_2026-09-09.md) · source SHA-256 `09974c0327d7307b1c30f8168d12fa68bb00babf8635c42cc2d3f1718131121e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-0CD25205E1D8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_contact_curvature_dichotomy_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=2c149e07284637ffe65c297e8ba6594ae898f579; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-circle contact-curvature and boundary co-neighbor dichotomy

**Date:** 2026-09-09  
**Repository base:** PR #119 after UF  
**Run type:** exact penny-graph curvature / local boundary geometry  
**Target:** post-ZF `x_B=o(D)` endpoint  
**Depends on:** C35 loaded degree cap, C65 full positive support, HB good hull-side coupling, UF face-defect floor  
**External web search:** not used  
**Computation:** decimal evaluation only

## LEVEL I STATUS

`STILL OPEN`

UF proves that every post-ZF sequence in the near-circle phase `x_B=o(D)` satisfies

```math
\frac QD\ge c_Q-o(1),
\qquad
c_Q=1.1013451504\ldots .
```

This report converts that face-degree defect into an exact vertex-curvature dichotomy.

Let `I=V(C)\setminus B_+` be the unloaded positive-contact vertices and let `n_j` count vertices of `I` of contact degree `j`. Define the loaded contact-degree slack

```math
s_B:=\sum_{b\in B_+}(3-\deg_C b)
=3q-e_{BI}-2e_{BB}\ge0.
```

Then

```math
\boxed{
s_B+n_3-n_5=4+x_B+Q.}
\tag{CV.1}
```

In particular, throughout the near-circle phase,

```math
\boxed{
s_B+n_3\ge(c_Q-o(1))D.}
\tag{CV.2}
```

Hence either at least `0.550672575D-o(D)` units of boundary loaded-degree slack occur, or at least that many unloaded trivalent vertices occur.

A second exact lemma constrains the first alternative geometrically. If three consecutive loaded hull vertices `A,B,C` have both hull sides `AB,BC` as unit contacts and the exterior turn at `B` is below `pi/3`, then `B` is the unique source point at unit distance from both `A` and `C`. Since the total exterior turning of the convex force hull is `2pi`, at most six good-good corners can fail this uniqueness test.

Thus the near-circle boundary has an almost-everywhere exact co-neighbor exclusion, simultaneously with the linear contact-curvature defect CV.2.

---

## 1. Unloaded contact degrees are between three and five

Every unloaded core vertex has no diameter reaction. Because the C65 relative-interior stress is positive on every incident actual contact, equilibrium at `v in I` is

```math
\sum_{vw\in C}\alpha_{vw}(p_v-p_w)=0,
\qquad
\alpha_{vw}>0.
\tag{1.1}
```

One or two nonzero contact vectors cannot positively span the origin in the planar positive-support setting without making the vertex collinear and non-extreme in the contact framework; the canonical force-visible equilibrium argument gives

```math
\deg_C(v)\ge3.
\tag{1.2}
```

Triangle-freeness gives the upper bound. If six unit-contact neighbors surrounded one vertex, their six cyclic angular gaps would each be at least `pi/3` by unit separation and would sum to `2pi`. Hence every gap would equal `pi/3`, making each consecutive neighbor pair unit distance apart and creating a unit triangle with the center. Therefore

```math
\boxed{3\le\deg_C(v)\le5\quad(v\in I).}
\tag{1.3}
```

C35 independently gives

```math
\boxed{\deg_C(b)\le3\quad(b\in B_+).}
\tag{1.4}
```

---

## 2. Exact contact-curvature identity

Euler and face incidence for the connected contact core give

```math
e=2v-2-\frac{b+Q}{2}.
\tag{2.1}
```

Therefore

```math
\boxed{
\sum_{u\in V(C)}(4-\deg_Cu)
=4v-2e
=4+b+Q.
}
\tag{2.2}
```

Split the vertex sum into loaded and unloaded vertices.

For loaded vertices,

```math
\sum_{b\in B_+}(4-\deg_Cb)
=q+s_B.
\tag{2.3}
```

For unloaded vertices, (1.3) gives

```math
\sum_{v\in I}(4-\deg_Cv)
=n_3-n_5.
\tag{2.4}
```

Since `b=q+x_B`, equations (2.2)-(2.4) give:

### Theorem CV.1 — exact vertex/face curvature balance

```math
\boxed{
s_B+n_3-n_5=4+x_B+Q.}
\tag{CV.3}
```

Equivalently,

```math
\boxed{
Q=s_B+n_3-n_5-x_B-4.
}
\tag{CV.4}
```

This is a purely combinatorial-geometric identity of the actual positive contact core. It does not use KKT weights beyond the degree bounds needed to identify the allowed unloaded degrees.

---

## 3. UF forces linear positive vertex curvature

In the near-circle phase,

```math
x_B=o(D)
```

and UF proves

```math
Q\ge(c_Q-o(1))D,
\qquad
c_Q=1.1013451504\ldots .
\tag{3.1}
```

From CV.3 and `n_5>=0`,

```math
\boxed{
s_B+n_3
\ge(c_Q-o(1))D.}
\tag{3.2}
```

Hence:

### Corollary CV.2 — boundary-slack / trivalent-interior dichotomy

Every near-circle post-ZF survivor satisfies at least one of

```math
\boxed{
s_B
\ge(0.5506725752\ldots-o(1))D}
\tag{3.3}
```

or

```math
\boxed{
n_3
\ge(0.5506725752\ldots-o(1))D.}
\tag{3.4}
```

This is not merely another face count. It says the mandatory `1.101D` exceptional-face degree is visible as a linear amount of positive contact-graph curvature: either on the loaded boundary through missing third contacts, or at unloaded trivalent vertices.

---

## 4. Good hull corners have an exact co-neighbor exclusion

Let `A,B,C` be three consecutive vertices of the convex force hull in cyclic order. Assume both hull sides are good unit contacts:

```math
|A-B|=|B-C|=1.
\tag{4.1}
```

Let `phi in (0,pi)` be the exterior turning angle at `B`. Thus the interior angle `ABC` is

```math
\pi-\phi.
```

The chord length is

```math
|A-C|
=2\cos\frac\phi2.
\tag{4.2}
```

The two unit circles centered at `A` and `C` meet at `B` and, unless tangent, at one other point `X`. The line `AC` bisects the segment joining the two circle-intersection points. Their distance is twice the altitude of the unit isosceles triangle with base `AC`, hence

```math
\boxed{|B-X|=2\sin\frac\phi2.}
\tag{4.3}
```

Suppose another source point `Y\ne B` is at unit distance from both `A` and `C`. The two circle intersections are exactly `B` and `X`, so `Y=X`. Unit separation in the source requires

```math
|B-X|\ge1.
```

By (4.3),

```math
2\sin\frac\phi2\ge1,
```

and therefore

```math
\boxed{\phi\ge\frac\pi3.}
\tag{4.4}
```

Thus:

### Theorem CV.3 — two-step boundary co-neighbor exclusion

If

```math
\phi<\frac\pi3,
```

then

```math
\boxed{
B\text{ is the unique source point at unit distance from both }A\text{ and }C.
}
\tag{CV.5}
```

The statement applies to all source points, including contact-isolated rattlers, not only to the positive core.

---

## 5. Only six good-good corners can fail the exclusion

For a convex polygon,

```math
\sum_{b\in B_+}\phi_b=2\pi.
\tag{5.1}
```

Therefore at most six hull vertices can have

```math
\phi_b\ge\pi/3.
\tag{5.2}
```

HB/DG gives `q-o(D)` good hull sides when `x_B=o(D)`. Consequently all but `o(D)` loaded hull vertices are incident to two good unit hull sides, and among those all but at most six satisfy CV.5.

### Corollary CV.4 — almost-everywhere boundary uniqueness

In the near-circle phase, at

```math
q-o(D)=\pi D-o(D)
```

loaded hull vertices `B`, the two second-neighbor loaded vertices `A,C` have no common unit neighbor other than `B` itself.

This excludes a common local mechanism for attaching the interior directly across two consecutive unit boundary edges.

---

## 6. Meaning of the boundary-slack branch

At a loaded vertex incident to two good hull sides, the two hull contacts are already present. C35 gives contact degree at most three. Hence its contribution to `s_B=3-deg_C` is

- `1` if it has no third contact;
- `0` if it has exactly one additional contact.

Only `o(D)` loaded vertices fail to have two good hull contacts. Therefore

```math
s_B
=
\#\{\text{double-good loaded vertices of degree }2\}
+o(D).
\tag{6.1}
```

Thus the first branch of CV.2 has a concrete interpretation:

> at least `0.550672575D-o(D)` loaded vertices lie on the almost complete unit-contact hull cycle and have no third contact into the rest of the core.

The second branch says instead that the core contains at least the same linear number of unloaded trivalent vertices.

---

## 7. Why this is not yet a contradiction

The regular odd-shell regression has essentially every loaded vertex of contact degree two, so the boundary-slack branch by itself is compatible with a non-global local minimum. Likewise a quadrangulated core can accommodate linearly many trivalent defects around exceptional faces.

The new restriction is the combination:

- near-isodiametric disk-like force hull;
- almost complete exact unit-contact boundary cycle;
- almost-minimally spaced diameter directions from DS;
- `Q>=1.101345D-o(D)` from UF;
- and either a linear population of boundary degree-two terminals or a linear population of unloaded trivalent vertices;
- plus CV.4 forbidding second-neighbor co-attachments at almost every hull corner.

A closing theorem must use global packing optimality or KKT transport to show that neither curvature branch can carry the required dense interior without a unit triangle or a strict diameter decrease.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Unloaded positive-core vertices have contact degree 3,4,or5; loaded vertices have
degree <=3. Euler gives exactly
    sum_v(4-deg v)=4+b+Q.
Writing s_B=sum_B(3-deg b), n_j=#unloaded degree-j vertices, b=q+x_B:
    s_B+n_3-n_5=4+x_B+Q.

UF in x_B=o(D) gives Q/D>=c_Q=1.1013451504..., hence
    s_B+n_3 >=(c_Q-o(1))D.
So either
    s_B>=0.5506725752D-o(D),
or
    n_3>=0.5506725752D-o(D).

Boundary lemma: for three consecutive loaded hull vertices A,B,C with AB=BC=1 and
exterior turn phi at B, the other common unit-circle intersection X of A,C satisfies
    |B-X|=2 sin(phi/2).
Thus a second source point at unit distance from both A,C requires phi>=pi/3.
Since total hull turning is 2pi, at most six good-good hull corners admit such a
second common unit neighbor.
```
