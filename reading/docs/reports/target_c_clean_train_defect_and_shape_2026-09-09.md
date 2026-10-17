> Generated reading edition · [exact source](../../../docs/reports/target_c_clean_train_defect_and_shape_2026-09-09.md) · source SHA-256 `9c316092fb90daf19fe9e82b00a48974fc497c88727b7ff8076ea76aee82e103`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-743B0F18F622","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — clean-train defect and diameter-direction shape bounds

**Date:** 2026-09-09  
**Repository state:** `2c476b38ee07218bb17a594b397717866c58b971`  
**Run type:** closing-proof continuation / exact finite topology and convex-width audit  
**Target:** Target C Gate C-II / Z route  
**External web search:** used for orientation only; no external theorem is a new proof dependency  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

This report proves two new exact reductions.

First, the stopped-train theorem DT has a finite convex-hull consequence that was not extracted in the September 9 campaign: a contact core with many convex-hull vertices must pay a linear amount of outer-walk or exceptional-face defect. In the ZF branch this forces the full diameter graph to have a linear incidence excess above a matching.

Second, the new ZF lower bound `h>=ceil(D)` can be fed back into C67's diameter-direction separation theorem. This raises the force-hull area floor from `0.5 sin(1/4) D^2` to asymptotically `0.5 sin(1) D^2`, and Cauchy's width formula gives a new primal force-hull perimeter lower bound. Combining that perimeter bound with the still-required ZF inequality `b+Q<=2h` closes every branch with too few diameter edges and forces

```math
\liminf \frac hD\ge 1.4781702664\ldots .
```

None of these statements proves the final exact face inequality. The surviving obstruction is narrower and more rigid, but Level I remains open.

## 1. Starting endpoint and notation

Let `G` be the connected nonisolated contact core of the lexicographically normalized hypothetical triangle-free global minimizer. Write

- `v,e` for its vertices and contact edges;
- `R` for bounded quadrilateral faces;
- `f` for bounded nonquadrilateral faces;
- `b` for the outer-face boundary-walk length, bridges counted twice;
- `Q=sum_(F non4)(deg F-4)`;
- `q` for the number of vertices of the strict convex hull of the core;
- `T` for the stopped-train count from DT;
- `h` for the number of actual diameter pairs.

The audited DT identity is

```math
\boxed{
2T=b+Q+4f.
}
\tag{1.1}
```

The audited ZF branch gives

```math
e+h\ge2v-2,
\tag{1.2}
```

while Euler gives

```math
e=2v-2-\frac{b+Q}{2}.
\tag{1.3}
```

Hence every ZF survivor satisfies

```math
\boxed{b+Q\le2h.}
\tag{1.4}
```

The September 9 ZS boundary-surplus report further gives

```math
\boxed{q\ge h\ge\delta\ge\lceil D\rceil.}
\tag{1.5}
```

The exact Level I scalar endpoint is still the strict reverse of (1.4):

```math
\boxed{b+Q>2h.}
\tag{1.6}
```

## 2. Clean trains force finite contact-topology defect

Put

```math
r:=b-q\ge0.
\tag{2.1}
```

The quantity `r` measures the excess length of the outer contact walk over the number of strict hull sides.

### Theorem ZD — finite clean-train defect inequality

For every finite connected straight-line unit-contact graph of a unit-separated triangle-free planar point set with at least three strict convex-hull vertices, using the DT notation above,

```math
\boxed{
T\le2r+Q+4f+2.
}
\tag{ZD.1}
```

Consequently

```math
\boxed{
q\le3r+Q+4f+4,
}
\tag{ZD.2}
```

and, since every bounded nonquadrilateral face has degree at least five and hence `f<=Q`,

```math
\boxed{
3r+5Q\ge q-4.
}
\tag{ZD.3}
```

In particular, with

```math
d_C:=b+Q-q=r+Q,
\tag{ZD.4}
```

one has the unweighted defect bound

```math
\boxed{
 d_C\ge\left\lceil\frac{q-4}{5}\right\rceil.
}
\tag{ZD.5}
```

This theorem is finite. It has no global-optimality, KKT, density, rattler-population, disk-topology, or asymptotic hypothesis.

### Proof

DT constructs the train graph by taking contact edges as vertices and joining opposite sides of each bounded rhombus. Every train component is a path. An incidence of a contact edge with the outer face or with a bounded nonquadrilateral face is exactly one terminal incidence of its train. A singleton train has two such incidences, possibly two occurrences of the same bridge on the outer walk. Thus the DT identity may be read as the exact endpoint count

```math
2T=b+\sum_{F\text{ non4}}\deg F=b+Q+4f.
\tag{2.2}
```

#### Step 1. Only `2r` outer train-end incidences can fail to be direct hull sides

Use the outer-walk partition already established in the proof of DE: choose the distinguished outer-face visit at every strict convex-hull vertex, in hull order, and partition the outer boundary walk into `q` walks between consecutive hull vertices. Let their positive integer lengths be

```math
\ell_1,\ldots,\ell_q,
\qquad
\sum_i\ell_i=b=q+r.
\tag{2.3}
```

Call an outer train-end incidence **good** if it is the unique edge occurrence in a length-one walk. Such an edge is the straight hull side between the corresponding consecutive strict hull vertices.

Let

```math
s:=|\{i:\ell_i>1\}|.
```

Because

```math
r=\sum_i(\ell_i-1),
```

every long walk contributes at least one, so `s<=r`. The number of outer incidences lying in long walks is

```math
\sum_{\ell_i>1}\ell_i
=b-(q-s)=r+s\le2r.
\tag{2.4}
```

Therefore at most `2r` outer train-end incidences are not good.

This incidence formulation is important: if an outer bridge is traversed twice, its two occurrences are counted separately. For `q>=3`, a singleton bridge cannot have both occurrences as good incidences, because the same unordered hull pair cannot be two different consecutive hull sides.

#### Step 2. Exceptional faces contribute exactly `Q+4f` bad endpoint incidences

Every incidence at a bounded nonquadrilateral face is, by definition, not a good outer incidence. Their exact number is

```math
\sum_{F\text{ non4}}\deg F=Q+4f.
\tag{2.5}
```

Call a train **clean** if both of its terminal incidences are good outer incidences. Every nonclean train contains at least one incidence among the at most

```math
2r+Q+4f
\tag{2.6}
```

bad endpoint incidences. Distinct trains have disjoint terminal incidences, so choosing one bad terminal incidence from each nonclean train gives an injection. Hence

```math
T_{\rm nonclean}\le2r+Q+4f.
\tag{2.7}
```

#### Step 3. There are at most two clean trains

A clean train has two endpoint contact edges that are actual sides of the strict convex hull. All contact edges belonging to one train are parallel, so those two hull sides have the same projective direction.

A strictly convex polygon has at most two sides in any fixed projective direction. Thus two distinct clean trains cannot have the same projective direction.

Now take two clean trains with distinct projective directions. Traverse the strict convex hull counterclockwise. If the two projective directions are represented by oriented side directions `theta` and `phi` with

```math
theta<phi<theta+\pi,
```

then the four corresponding hull sides occur in cyclic tangent-direction order

```math
theta,\quad phi,\quad theta+\pi,\quad phi+\pi.
\tag{2.8}
```

Therefore the two pairs of side midpoints alternate on the boundary of the convex hull.

A clean train cannot be a singleton: for `q>=3` a singleton outer bridge cannot have both outer occurrences good, as noted above. Its DT midpoint curve is therefore a simple proper polygonal arc inside the convex hull, with interior disjoint from the hull boundary. Two such arcs whose four endpoints alternate on the boundary of a disk must intersect.

Distinct DT train curves cannot meet at a contact-edge midpoint, because every contact edge belongs to exactly one train component. Interiors of different bounded faces are disjoint. Hence an intersection of two distinct train curves occurs inside a common rhombus, where the two midpoint segments cross. Thus any two clean trains are adjacent in the DT train-crossing graph.

DT proves that train-crossing graph is triangle-free. Therefore three clean trains are impossible:

```math
\boxed{T_{\rm clean}\le2.}
\tag{2.9}
```

Combining (2.7) and (2.9) proves (ZD.1).

Finally use the exact endpoint identity (1.1):

```math
q+r+Q+4f=2T
\le4r+2Q+8f+4,
```

so

```math
q\le3r+Q+4f+4,
```

which is (ZD.2). A bounded face of a simple triangle-free contact graph contains a cycle of length at least four; if its face walk is not a quadrilateral, its degree is at least five. Hence `f<=Q`, giving

```math
q\le3r+5Q+4\le5(r+Q)+4.
```

This proves (ZD.3) and (ZD.5). QED.

## 3. Exact consequences in the ZF survivor

For a ZF survivor define the diameter-incidence excess

```math
k_H:=2h-q.
\tag{3.1}
```

There are no isolated vertices in the diameter graph on `B`, so `k_H>=0`. Equation (1.4) is exactly

```math
q+d_C=b+Q\le2h=q+k_H,
```

hence

```math
\boxed{d_C\le k_H.}
\tag{3.2}
```

ZD therefore gives a new linear lower bound on the diameter incidence surplus:

```math
\boxed{
2h-q
\ge
\left\lceil\frac{q-4}{5}\right\rceil.
}
\tag{3.3}
```

Equivalently,

```math
\boxed{
h\ge\left\lceil\frac{3q-2}{5}\right\rceil.}
\tag{3.4}
```

Thus the full diameter graph of any large ZF survivor is quantitatively denser than a matching:

```math
\liminf\frac hq\ge\frac35.
\tag{3.5}
```

Because the current ZS report gives `q>=ceil(D)`, also

```math
\boxed{
d_C\ge\left\lceil\frac{\lceil D\rceil-4}{5}\right\rceil.}
\tag{3.6}
```

### Corollary ZD.1 — the matching phase is eliminated

If `H` were a matching on its `q` nonisolated terminals, then `2h-q=0`. Equation (3.3) would force `q<=4`. Hence no sufficiently large ZF survivor has a matching diameter graph.

This is an exact support statement. It uses no lower bound on the `beta` weights.

### Corollary ZD.2 — tree-component count

Use the standard planar diameter-graph characterization already recorded in Target C: every connected component is a caterpillar whose spine may close into one odd cycle. Let `t_H` be the number of tree components. Every tree component contributes one fewer edge than vertices and every unicyclic component contributes equal numbers, so

```math
h=q-t_H.
\tag{3.7}
```

Equation (3.3) becomes

```math
q-2t_H\ge\frac{q-4}{5},
```

and therefore

```math
\boxed{t_H\le\left\lfloor\frac{2q+2}{5}\right\rfloor.}
\tag{3.8}
```

In particular a forest survivor has at most about `0.4q` diameter components. The previous geometric diameter-graph bound allowed a crossing matching with `q/2` components.

## 4. ZF amplifies the C67 force-hull area floor

C67 proves that any two distinct actual diameter edges have projective direction separation at least

```math
\delta_D:=2\arcsin\frac1{2D}.
\tag{4.1}
```

It also proves the following circle-packing statement: for `h` such directions, two have projective circular distance at least

```math
\min\left\{\frac\pi3,(h-1)\delta_D\right\}.
\tag{4.2}
```

The original C67 report had only the older lower bound `h>D/4`, producing the asymptotic angle `1/4` and the area coefficient `0.5 sin(1/4)`.

Under ZF, ZS now gives `h>=ceil(D)`. Therefore put

```math
\Phi_Z(D):=
\min\left\{
\frac\pi3,
(\lceil D\rceil-1)2\arcsin\frac1{2D}
\right\}.
\tag{4.3}
```

Exactly as in C67, two diameter chords with projective angle at least `Phi_Z(D)` span either a triangle or crossing convex quadrilateral of area at least

```math
\frac{D^2}{2}\sin\Phi_Z(D).
```

All their endpoints lie in the force hull `F`. Hence:

### Theorem ZA.1 — amplified force-hull area floor

Every sufficiently large ZF survivor satisfies

```math
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{2}\sin\Phi_Z(D).
}
\tag{ZA.1}
```

Since

```math
(\lceil D\rceil-1)2\arcsin\frac1{2D}\longrightarrow1<\frac\pi3,
```

```math
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac12\sin1
=0.4207354924\ldots .
}
\tag{ZA.2}
```

The old C67 coefficient was

```math
\frac12\sin\frac14=0.1237019796\ldots .
```

Thus ZF more than triples the certified area coefficient. The isodiametric maximum `pi/4` is `0.785398...`; ZA.2 says the force hull itself already occupies at least `53.57%` of that maximal area scale. This does not eliminate the fully inactive rattler population.

## 5. Diameter directions force a large primal perimeter

The same separated direction set gives more than a two-chord area estimate.

Let the `h` projective directions of the actual diameter edges be

```math
\alpha_1,\ldots,\alpha_h\in\mathbb R/\pi\mathbb Z
```

in cyclic order, and let `g_i` be the consecutive circular gaps, so

```math
g_i>0,
\qquad
\sum_i g_i=\pi.
\tag{5.1}
```

C67 gives `g_i>=delta_D` for every `i`.

Let `w_F(theta)` be the width of the force hull in direction `theta`. A diameter chord of length `D` and projective direction `alpha_i` has projected endpoint separation

```math
D\cos d_{\mathbb{RP}^1}(\theta,\alpha_i),
```

where the projective circular distance lies in `[0,pi/2]`. Hence

```math
w_F(\theta)
\ge
D\max_i\cos d_{\mathbb{RP}^1}(\theta,\alpha_i).
\tag{5.2}
```

Cauchy's width formula, already used in the shared shell theory, is

```math
\operatorname{per}(F)=\int_0^\pi w_F(\theta)\,d\theta.
\tag{5.3}
```

On the gap of length `g_i` between two consecutive diameter directions, the nearest endpoint direction is at distance `min(t,g_i-t)`. Therefore

```math
\int_{\text{gap }i}
\max_j\cos d(\theta,\alpha_j)\,d\theta
=2\sin\frac{g_i}{2}.
\tag{5.4}
```

Summing gives

```math
\boxed{
\frac{\operatorname{per}(F)}D
\ge
2\sum_{i=1}^h\sin\frac{g_i}{2}.
}
\tag{5.5}
```

The function `sin(x/2)` is concave on `[0,pi]`. Under the constraints

```math
g_i\ge\delta_D,
\qquad
\sum g_i=\pi,
```

the minimum of the concave sum occurs at an extreme point of the gap simplex: `h-1` gaps equal `delta_D`, and the remaining gap equals `pi-(h-1)delta_D`. Thus

```math
\operatorname{per}(F)
\ge
2D\left[
(h-1)\sin\frac{\delta_D}{2}
+
\sin\frac{\pi-(h-1)\delta_D}{2}
\right].
\tag{5.6}
```

Since

```math
\sin\frac{\delta_D}{2}=\frac1{2D},
```

we obtain the exact finite bound:

### Theorem ZA.2 — diameter-direction perimeter bound

Let

```math
a_D:=\arcsin\frac1{2D}.
```

Then every C65 force hull with `h` actual diameter edges satisfies

```math
\boxed{
\operatorname{per}(F)
\ge
(h-1)+2D\cos((h-1)a_D).
}
\tag{ZA.3}
```

No KKT weight appears in this inequality.

### Asymptotic ZF consequence

Along any hypothetical unbounded ZF sequence, pass to a subsequence on which

```math
\frac hD\to\tau.
```

C67 direction separation itself gives `h delta_D<=pi`, so `1<=tau<=pi` using ZS. Since `Da_D->1/2`, ZA.3 gives

```math
\liminf\frac{\operatorname{per}(F)}D
\ge
\tau+2\cos\frac\tau2.
\tag{5.7}
```

On `[1,pi]`,

```math
\frac d{d\tau}\left(\tau+2\cos\frac\tau2\right)
=1-\sin\frac\tau2\ge0.
```

Therefore:

```math
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{per}(F)}D
\ge
1+2\cos\frac12
=2.7551651238\ldots .
}
\tag{ZA.4}
```

For comparison, the universal upper bound is `per(F)<=pi D`.

## 6. The perimeter bound closes every low-h branch

Each of the `q` distinguished outer walks has geometric displacement equal to the corresponding hull side. By the triangle inequality, summing their unit edge lengths gives

```math
\boxed{b\ge\operatorname{per}(F).}
\tag{6.1}
```

A ZF survivor also satisfies `b+Q<=2h`, so in particular

```math
\operatorname{per}(F)\le2h.
\tag{6.2}
```

Combine this with ZA.3:

```math
(h-1)+2D\cos((h-1)a_D)\le2h.
\tag{6.3}
```

Equivalently,

```math
2D\cos((h-1)a_D)\le h+1.
\tag{6.4}
```

Let `tau_*` be the unique root in `(1,pi)` of

```math
\boxed{
\tau=2\cos\frac\tau2.
}
\tag{6.5}
```

Numerically,

```math
\boxed{
tau_*=1.4781702664\ldots .
}
\tag{6.6}
```

If a subsequence had `h/D->tau<tau_*`, then ZA.3 would give

```math
\frac{\operatorname{per}(F)}D
\ge
\tau+2\cos(\tau/2)+o(1)
>2\tau+o(1)
=\frac{2h}{D}+o(1),
```

contradicting (6.2). Therefore:

### Corollary ZA.3 — amplified diameter-edge density

Every unbounded hypothetical ZF sequence satisfies

```math
\boxed{
\liminf\frac hD\ge\tau_*
=1.4781702664\ldots .
}
\tag{ZA.5}
```

Since `q>=h`, the same lower bound holds for `q/D`.

This strengthens the current ZS bound `h/D>=1` without any response-magnitude input.

The ZS boundary surplus also improves immediately:

```math
\sigma_B=2q-\delta-2
\ge2h-\delta-2
\ge h-2,
```

because `delta<=h`. Hence

```math
\boxed{
\liminf\frac{\sigma_B}{D}\ge\tau_*.
}
\tag{ZA.6}
```

Finally `tau_*>pi/3`. Thus for all sufficiently large survivors the C67 two-direction lower bound has already reached its `pi/3` branch, giving the stronger eventual finite area floor

```math
\boxed{
\operatorname{area}(F)\ge\frac{\sqrt3}{4}D^2
}
\tag{ZA.7}
```

for all sufficiently large members of the sequence. This improves the asymptotic `0.5 sin 1` statement ZA.2 after the bootstrap.

## 7. Interaction with the new ZM response theorem

Current main also contains the independent report-level theorem ZM. It gives exact boundary-defect rank, mixed signs in every terminal row, and a terminal-disjoint matching of at least `q/16` strictly non-diameter response pairs.

ZD and ZA do not duplicate ZM:

- ZM is an electrical/stress theorem and still lacks a conductance floor;
- ZD is a finite contact-face/train theorem with no stress weights;
- ZA is a convex-width theorem using only the actual diameter support.

Together with ZA.5, ZM's support matching now has asymptotic cardinality at least

```math
\frac{q}{16}
\ge
\left(\frac{\tau_*}{16}+o(1)\right)D
=0.0923856\ldots D,
\tag{7.1}
```

although its total response conductance may still tend to zero.

## 8. Exact remaining obstruction

Define the Eppstein slack and mixed-rigidity row surplus

```math
r_E:=2v-\delta-2-e\ge0,
\qquad
s_Z:=e+h-(2v-2)\ge0.
\tag{8.1}
```

Euler gives the exact identity

```math
\boxed{
\frac{b+Q}{2}=\delta+r_E,
}
\tag{8.2}
```

while the definitions give

```math
\boxed{
h=\delta+r_E+s_Z.}
\tag{8.3}
```

Therefore

```math
\boxed{
2h-(b+Q)=2s_Z.
}
\tag{8.4}
```

The final scalar contradiction is exactly the statement that the mixed rigidity row surplus cannot be nonnegative for a sufficiently large global source. ZD and ZA shrink the class in which `s_Z>=0` could occur, but they do not themselves make `s_Z<0`.

After this report, a hypothetical survivor must simultaneously satisfy

```math
\begin{gathered}
q\ge h\ge(\tau_*+o(1))D,\\
2h-q\ge\left\lceil\frac{q-4}{5}\right\rceil,\\
d_C=b+Q-q\ge\left\lceil\frac{q-4}{5}\right\rceil,\\
\operatorname{per}(F)\ge(2.755165\ldots+o(1))D,\\
\operatorname{area}(F)\ge\frac{\sqrt3}{4}D^2\quad\text{eventually},\\
2h-(b+Q)=2s_Z\ge0.
\end{gathered}
\tag{8.5}
```

The shortest remaining theorem is still

```math
\boxed{b+Q>2h.}
```

A genuinely new route must now use one of the near-equality consequences hidden in (8.5), or convert ZM's linear response matching into quantitative mass.

## 9. Regression and scope audit

### Regular odd shells

A regular unit odd polygon has a shell contact graph and can violate the desired face inequality, but it is not a large global minimum-diameter source. ZD is compatible with it: the unique bounded face has degree `q`, so `Q=q-4`, providing the required contact-topology defect.

### Regular even cycle with opposite diameter matching

Regular even unit polygons provide exact PSD affine-kernel cycle-vs-opposite-matching stresses for arbitrarily large even `q`. They show that terminal stress rank/sign data alone cannot exclude `h=q/2`. They do not contradict ZD because they fail ZF for large `q`: their mixed row count is too small. ZD+ZF excludes this matching phase exactly.

### Pure rhombic disks

When `Q=f=0`, ZD sharpens to

```math
q\le3(b-q)+4.
```

This is only a finite topology estimate. The much stronger asymptotic exposed-hull theorem used by ZB remains the correct tool for dense globally minimizing pure disks.

### Bridges and repeated outer walks

The proof uses outer-face **incidences**, not distinct edge identities. A bridge traversed twice contributes two outer endpoint incidences, exactly as in DT. The distinguished-visit partition from DE places every repeated occurrence inside one of the `q` outer walks, so (2.4) retains all bridge excursions.

### Holes and multiple rhombic components

No disk assumption is used. Clean train curves are simple arcs lying in the convex hull. Alternating endpoints force intersection as plane arcs whether or not the contact graph has exceptional holes. The intersection can only occur in a common rhombus by the DT construction.

### Face-local Oler regression

The DP pentagons with vanishing Oler excess remain binding. ZD charges an exceptional pentagon combinatorially through its five train-end incidences; it does not assert any uniform positive area excess for that face.

### Rattlers

No theorem here bounds the number of fully inactive source points. C65's strict rattlers remain a live global-capacity obstruction. ZA.7 makes their admissible force-hull geometry substantially narrower but does not count them.

## 10. Failed routes and no-go conclusions

1. **Terminal PSD rank alone.** Dead as a closing route. Regular even polygons support exact maximal-rank PSD stresses with a diameter matching.
2. **Strict response support implies mass.** Still false without a new mechanical conductance estimate; ZM gives linear support but no aggregate lower conductance.
3. **Face-local positive Oler charge.** Dead by DP.
4. **Matching or near-matching diameter support.** Now closed under ZF by ZD. Any survivor has `h/q>=3/5-o(1)`.
5. **Low diameter-edge density `h/D<tau_*`.** Now closed asymptotically by ZA.3 and the ZF face inequality.

## 11. Promotion recommendation

**Hold as report pending independent review.**

If the proofs survive review, the natural canonical changes are:

- add ZD to the general-topology train frontier;
- update the ZF/Z route with (3.3)–(3.6);
- update C67's force-hull area module with ZA.1–ZA.7;
- update the active continuation prompt so future runs start from `h/D>=tau_*`, not merely `h/D>=1`;
- retain the exact Level I status as open.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New finite train theorem ZD:
For r=b-q,
    T <= 2r+Q+4f+2,
    q <= 3r+Q+4f+4,
    3r+5Q >= q-4,
    d_C=b+Q-q >= ceil((q-4)/5).
Proof: at most 2r bad outer endpoint incidences, exactly Q+4f exceptional
endpoint incidences, and at most two clean hull-to-hull trains because clean
trains pairwise cross while the DT crossing graph is triangle-free.

ZF consequence:
    d_C <= 2h-q,
so
    2h-q >= ceil((q-4)/5),
    h >= ceil((3q-2)/5).
Matching diameter support is impossible for q>4.

New diameter-direction shape theorem ZA:
C67 gives direction separation delta_D=2 asin(1/(2D)).
ZF/ZS gives h>=ceil D.
Therefore
    area(F) >= (D^2/2) sin(min(pi/3,(ceil D-1)delta_D)),
    liminf area(F)/D^2 >= 0.5 sin 1.

Cauchy width formula plus the complete direction set gives the exact bound
    per(F) >= (h-1)+2D cos((h-1) asin(1/(2D))).
Since b>=per(F) and ZF requires b+Q<=2h, every unbounded survivor satisfies
    liminf h/D >= tau_*=1.4781702664...,
where tau_*=2 cos(tau_*/2).
Hence eventually
    area(F) >= sqrt(3) D^2/4,
    liminf sigma_B/D >= tau_*.

Exact remaining obstruction:
With r_E=2v-delta-2-e and s_Z=e+h-(2v-2),
    (b+Q)/2=delta+r_E,
    h=delta+r_E+s_Z,
so
    2h-(b+Q)=2s_Z.
The final theorem still must force s_Z<0, equivalently b+Q>2h.

Authoritative dependencies:
- campaign_defect_train_extension_2026-09-09.md (DT/DE endpoint-incidence topology)
- target_c_zf_boundary_surplus_collapse_2026-09-09.md (q>=h>=delta>=ceil D)
- target_c_force_hull_area_floor_2026-08-31.md (C67 direction separation)
- docs/theory/03-oler-shell.md (Cauchy width formula)
- campaign_boundary_defect_matching_2026-09-09.md (independent ZM response theorem)
```
