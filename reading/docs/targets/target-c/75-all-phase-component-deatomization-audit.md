> Generated reading edition · [exact source](../../../../docs/targets/target-c/75-all-phase-component-deatomization-audit.md) · source SHA-256 `39553cf0e644b37e1b7d81c6a9cc367e3e652532f5303c84436b8edab63d40c3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — all-phase component deatomization audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module independently rebuilds the strongest valid theorem from the unreviewed
report `target_c_all_phase_component_deatomization_2026-09-11.md` using only the
current canonical post-ZF stack. The compactness prelude of that report is unnecessary:
a finite curvature-window argument gives a uniform estimate and the quantitative
conclusion

$$
\boxed{c_I=O(D^{2/3})}
$$

in every sufficiently large post-ZF C-II survivor, in both Woodall branches and for
arbitrary `s_Z>=0`.

Contact-isolated source points are not counted by `c_I`; they remain in the full
source and are not bounded by this theorem.

---

# 75. Unloaded harmonic components are sublinear in every post-ZF phase

Use the canonical notation:

- `F` is the full positive force hull and `B=Vert(F)`, `q=|B|`;
- `I_1,...,I_{c_I}` are the connected components of the unloaded positive-contact
  graph after deleting `B` from the nonisolated positive-contact core;
- `A_r subset B` is the distinct loaded attachment set of `I_r`;
- `delta_r` is the graph diameter of `C[I_r]`, with `delta_r=0` for a singleton;
- `e_BB` is the loaded-loaded contact count;
- `s_C` is the total extra pinned-contact left-nullity;
- `k=d_H+s_Z`.

The proof uses the following canonical facts.

1. Every unloaded positive-contact vertex has contact degree `3`, `4`, or `5`.
2. Every loaded vertex has contact degree at most three.
3. Harmonic trapping gives
   $$
   I_r\subset\operatorname{conv}(A_r),
   \qquad |A_r|\ge3,
   \qquad \operatorname{diam}(A_r)\le\delta_r+2.
   \tag{75.1}
   $$
4. Canonical Section 62 gives
   $$
   c_I+e_{BB}+s_C=q-2+k
   \tag{75.2}
   $$
   and
   $$
   \sum_r\delta_r+R_I+s_B+3k=6+e_{BB}+2s_C,
   \qquad R_I,s_B\ge0.
   \tag{75.3}
   $$
5. Canonical full-force stability gives
   $$
   \liminf {\operatorname{area}(F)\over D^2}
   \ge {2\rho+\sin(2\rho)\over4}
   =0.6184708847\ldots>{3\over5},
   \tag{75.4}
   $$
   while canonical full-source geometry places `F` inside the source circumdisk of
   radius
   $$
   {D\over2}+3^{1/4}\sqrt D.
   \tag{75.5}
   $$

No KKT coefficient floor, disk-limit theorem, cap containment, or deletion of source
isolates is used.

## 75.1 Three unit neighbors cannot fit in a strip thinner than one half

### Lemma 75.1

Let `x` and three distinct unit neighbors of `x` belong to a unit-separated planar
set. The four points cannot all lie in a strip of width strictly less than `1/2`.

**Proof.** Let `n` be a unit normal to the strip. For a unit neighbor direction `u`,
all four points lying in a strip of width `<1/2` implies

$$
|n\cdot u|<1/2.
$$

On the unit circle the allowed directions form two open arcs, each of angular width
`pi/3`, centered on the two strip-tangent directions. Two distinct unit neighbors in
one such arc have angular separation `<pi/3`, hence mutual distance `<1`, contrary to
unit separation. Thus at most one neighbor lies in each allowed arc, so at most two
unit neighbors exist. Contradiction. `square`

## 75.2 A finite curvature window for every bounded component

The finite theorem is easiest to state for a fat force hull.

### Theorem 75.2

Suppose

$$
B(o,D/20)\subset F\subset B(o,11D/20).
\tag{75.6}
$$

For an integer `M>=0`, let

$$
N_M:=\#\{r:\delta_r\le M\}.
$$

Then

$$
\boxed{N_M\le5000\pi(M+2)^2.}
\tag{75.7}
$$

The constant is deliberately coarse and uniform in the source, stresses, component
population, and `D`.

**Proof.** Translate `o` to the origin and put

$$
L:=M+2\ge2,
\qquad r:=D/20,
\qquad R:=11D/20.
$$

First handle `L>D/10000`. Every unloaded component has at least three distinct loaded
attachments by (75.1). A loaded vertex belongs to at most three attachment sets because
its full contact degree is at most three. Hence `c_I<=q`. The loaded vertices form a
unit-separated convex polygon, so

$$
q\le\operatorname{per}(F)\le\pi D.
$$

Therefore

$$
N_M\le\pi D<10000\pi L\le5000\pi L^2,
$$

using `L>=2`.

Assume now

$$
L\le D/10000.
\tag{75.8}
$$

For each counted component choose one representative attachment `b in A_r`. Every
other attachment `a in A_r` satisfies `|a-b|<=L` by (75.1). Since all boundary radii
are at least `r`, the minor polar separation `alpha` between `a` and `b` obeys

$$
2r\sin(\alpha/2)\le |a-b|\le L.
$$

Using `arcsin t<=2t` for `0<=t<=1/2`,

$$
\alpha\le {2L\over r}\le {1\over250}.
\tag{75.9}
$$

Let

$$
e:={b\over|b|}.
$$

Follow the local boundary arc of `F` from `b` to one other attachment `a`. At a point
`p` of that arc let `n` be an outward unit normal. The inner and outer disk bounds give

$$
n\cdot {p\over|p|}\ge {r\over R}={1\over11}.
$$

Every point of the local arc has polar direction within `alpha` of `e`, so by (75.9)

$$
n\cdot e\ge {1\over11}-{1\over250}>{1\over22}.
\tag{75.10}
$$

For the counterclockwise unit tangent `t=Jn`, (75.10) gives

$$
t\cdot Je>{1\over22}.
$$

The `Je`-projection changes by at most `|a-b|<=L` between the arc endpoints. Hence the
boundary arclength from `b` to `a` is at most

$$
w:=22L.
\tag{75.11}
$$

Thus every attachment of the counted component lies in the boundary-arclength window
of radius `w` centered at its representative.

Put

$$
\theta:=\arctan {1\over4L}.
\tag{75.12}
$$

The radius-`w` window about every representative must carry exterior turning at least
`theta`. Otherwise all edge tangents on that convex boundary window lie in a cone of
angular width `<theta`. Take the first and last attachments of the component in
boundary order. Their Euclidean distance is at most `L`, and tangent projection along
the first tangent direction is monotone. The transverse variation of their intervening
arc, hence of all attachments and their convex hull, is at most

$$
L\tan\theta={1\over4}<{1\over2}.
$$

By harmonic trapping, `I_r` lies in the same strip. Any unloaded vertex of `I_r` and
all of its contact neighbors lie in `I_r union A_r`, hence in that strip, contradicting
Lemma 75.1 because the unloaded vertex has at least three unit-contact neighbors.
Therefore the window turning is at least `theta`.

Choose a maximal family of representative attachments with pairwise circular boundary
arclength distance greater than `2w`. Their radius-`w` windows are disjoint, so the
convex boundary's total exterior turning `2pi` gives at most

$$
{2\pi\over\theta}
\tag{75.13}
$$

chosen representatives. Maximality implies that every representative lies in a
radius-`2w` window about one chosen representative.

A radius-`2w` boundary window has total arclength `4w` and contains at most `4w+1`
loaded vertices, because consecutive loaded vertices are at Euclidean, hence boundary
arclength, distance at least one. Each loaded vertex can represent at most three
components. Consequently

$$
N_M\le {2\pi\over\theta}\,3(4w+1).
\tag{75.14}
$$

Since `L>=2`,

$$
\theta=\arctan(1/(4L))\ge {1\over8L}.
$$

Together with `w=22L`, (75.14) yields

$$
N_M\le48\pi L(88L+1)
\le4248\pi L^2
<5000\pi L^2.
$$

This proves (75.7). `square`

## 75.3 Every large canonical force hull is fat enough

### Lemma 75.3

For every sufficiently large post-ZF C-II survivor, after translating by the canonical
source circumcenter `o`,

$$
B(o,D/20)\subset F\subset B(o,11D/20).
\tag{75.15}
$$

**Proof.** By (75.4), for all sufficiently large survivors

$$
\operatorname{area}(F)>{3\over5}D^2.
\tag{75.16}
$$

By (75.5), the outer inclusion in (75.15) also holds for all sufficiently large `D`.

For every unit direction `u`, the bounding rectangle of `F` with one side parallel to
`u` gives

$$
\operatorname{area}(F)
\le D\,\operatorname{width}_F(u).
$$

Hence (75.16) implies

$$
\operatorname{width}_F(u)>{3D\over5}.
$$

Writing support functions relative to `o`, the outer disk gives

$$
h_F(-u)\le {11D\over20}.
$$

Therefore

$$
h_F(u)=\operatorname{width}_F(u)-h_F(-u)>{D\over20}
$$

for every unit `u`. This is exactly the inner disk inclusion in (75.15). `square`

## 75.4 Quantitative all-phase component count

### Theorem 75.4

Every sufficiently large post-ZF C-II survivor satisfies

$$
\boxed{c_I=O(D^{2/3}).}
\tag{75.17}
$$

More explicitly, for every integer `M>=1`,

$$
\boxed{
c_I
\le5000\pi(M+2)^2
+{2+2\pi D\over M+1}.
}
\tag{75.18}
$$

**Proof.** Lemma 75.3 permits Theorem 75.2. It remains to control components with
`delta_r>M`.

From (75.3), eliminating `s_C` with (75.2) gives

$$
\sum_r\delta_r
\le 2+2q-e_{BB}-k-2c_I
\le2+2q
\le2+2\pi D.
\tag{75.19}
$$

Every component not counted by `N_M` has integer graph diameter at least `M+1`, so

$$
c_I\le N_M+{2+2\pi D\over M+1}.
$$

Use (75.7) to obtain (75.18). Taking

$$
M=\lfloor D^{1/3}\rfloor
$$

proves (75.17). `square`

## 75.5 Exact ledger consequences

The component theorem has immediate exact asymptotic consequences, but they must keep
the canonical meanings of all variables straight.

From (75.2),

$$
\boxed{
e_{BB}+s_C=q+k+O(D^{2/3}).}
\tag{75.20}
$$

Let `m_B` denote the number of nonunit force-hull sides, the quantity called `m` in
Section 63. Section 63 gives

$$
e_{BB}=q-m_B+c_B,
\tag{75.21}
$$

where `c_B>=0` counts loaded-loaded contacts beyond the unit convex-hull sides.
Combining (75.21) with (75.2) gives the exact identity

$$
m_B+k=c_I+c_B+s_C+2,
$$

and therefore

$$
\boxed{m_B+k=c_B+s_C+O(D^{2/3}).}
\tag{75.22}
$$

For the canonical renormalized surplus

$$
\mu_DD:=e_{BB}+2s_C-3k,
$$

(75.2) gives

$$
\boxed{
\mu_DD
=q+s_C-2k+O(D^{2/3})
=2q-e_{BB}-k+O(D^{2/3}).
}
\tag{75.23}
$$

Since `s_C>=0` and canonical difference-body density gives

$$
\liminf {q\over D}\ge\liminf {h\over D}\ge2\rho,
\qquad \rho=\cos\rho,
$$

we obtain the useful all-phase inequality

$$
\boxed{
\liminf\left(\mu_D+{2k\over D}\right)\ge2\rho
=1.478170\ldots .
}
\tag{75.24}
$$

In particular, on any subsequence with `k=o(D)`,

$$
\boxed{\liminf\mu_D\ge2\rho.}
\tag{75.25}
$$

More quantitatively, if a subsequence has `mu_D->mu`, then

$$
\boxed{
\liminf {k\over D}\ge {2\rho-\mu\over2}
}
\tag{75.26}
$$

whenever the right side is positive. Thus a sequence approaching the old
`z_*>0.9604` renormalized-surplus frontier must carry a genuinely linear topology/rank
defect `k`; it cannot lie in `k=o(D)`.

These are structural reductions, not contradictions.

## 75.6 What the theorem does not control

The bound (75.17) concerns unloaded components of the **nonisolated positive-contact
core** only. It does not bound:

- contact-isolated source points;
- the total population inside the surviving `O(D^{2/3})` components;
- `sum delta_r` below its existing `O(D)` bound;
- source population in inward pockets or outside `F`;
- individual KKT weights;
- simultaneous rearrangeability of distinct attachment cells.

Sublinear component count alone does not prove a full-source packing/slack inequality.

## 75.7 Dependency and regression audit

- **Unloaded degree >=3:** canonical C26; no neutral degree-one/two transport is used.
- **Loaded degree <=3:** canonical C35.
- **Harmonic trapping / attachment diameter:** canonical C36/C40 and the all-phase
  rederivation in Section 62.
- **All-phase component diameter ledger:** canonical (62.14); no near-minimal
  `sigma_B=o(D)` assumption is used.
- **Fat force hull:** canonical full-force area stability plus the canonical source
  circumradius bound.
- **Contact isolates:** retained globally and explicitly outside `c_I`.
- **Corner concentration:** the canonical theorem uses the finite curvature-window
  proof, not a smooth/disk-limit assumption.
- **Rejected Reuleaux cap:** unused.
- **KKT coefficient floors:** unused.
- **Eppstein equality/near-quadrangulation:** unused.

## 75.8 Compact handoff

```text
all post-ZF C-II survivors
  -> F contains B(o,D/20) and lies in B(o,11D/20)
  -> component with delta_r<=M has attachment diameter <=M+2
  -> its representative boundary window must spend >=atan(1/(4(M+2))) turning
  -> bounded components N_M <=5000*pi*(M+2)^2

canonical component-diameter budget:
  sum delta_r <=2+2*pi*D

choose M=floor(D^(1/3)):
  c_I=O(D^(2/3)).

Exact consequences:
  e_BB+s_C=q+k+O(D^(2/3)),
  m_B+k=c_B+s_C+O(D^(2/3)),
  mu_D D=q+s_C-2k+O(D^(2/3)),
  liminf(mu_D+2k/D)>=2rho.

Remaining gap:
  convert these sublinear-component reductions into a full-source slack/capacity or
  response contradiction; source isolates and total component populations remain.
```
