> Generated reading edition · [exact source](../../../docs/reports/target_c_pure_rhombic_zf_exclusion_2026-09-11.md) · source SHA-256 `7fe22200233ec3d86bdff47395c884dac966cddd289f2250339af0aff05dd39f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-1298EAE74691","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact pure-rhombic C-II exclusion

**Date:** 2026-09-11  
**Run type:** Target C-II / exact subbranch exclusion  
**Status:** unpromoted research report; no route-map status is changed

## LEVEL I STATUS

`STILL OPEN`.

The source-carrying case is the previously audited ZB contradiction; the new
content here is its isolate-robust extension.  It proves a complete contradiction
for the exact simply connected pure-rhombic subbranch of C-II when the pure
rhombic contact core has only boundary-order isolates.  The same proof remains
valid when the pure rhombic contact core
has only (O(D)) contact-isolated source points, provided the phase estimate
is applied to that actual dense core.  It does not promote the stronger
assertion that every C-II source has this topology, and it does not discard
contact-isolated sources in the unrestricted problem.

The contradiction is particularly short once the two exact ledgers are kept
together:

```math
s_Z=e+h-(2v-2)=h-T,
```

where (T) is the number of train tracks.  Thus (s_Z\ge0) forces (h\ge T).
The audited pure-disk phase theorem gives (q/T\le0.9039456812+o(1)), while
all diameter endpoints are among the (q) convex-hull vertices, so
```math
h\le q<T
```
for sufficiently large sources.  This contradicts ZF.

## 1. Exact hypotheses

Let (A) be a triangle-free global minimizer in the Target C-II normalization:
contacts are minimized first, diameter pairs second, and the actual contact and
diameter rows are the selected strong rows.  Let (G_C) be its nonisolated
contact graph, with (v=|V(G_C)|), (e=|E(G_C)|), and (h=|H|).

Assume the following additional, explicit subbranch hypotheses.

1. (G_C) is the 1-skeleton of a finite simply connected pure strict-rhombic
   disk: every bounded contact face is a unit rhombus, the bounded faces form a
   topological disk, and every vertex of the nonisolated core is a vertex of
   this complex.  Either there are no contact-isolated sources, or their number
   is (O(D)).
2. The core has diameter (D).  Equivalently for this argument, the actual
   diameter endpoints used below all lie in this core.
3. The pure-disk phase theorem of Target B applies to this actual contact core.
   In particular, if (R) is the number of rhombi, (T) the number of train
   tracks, and (q) the number of convex-hull vertices, then
   
   ```math
   \frac qT\le0.9039456812+o(1).
   \tag{PR.1}
   ```


The first hypothesis is deliberately weaker than source-carrying purity.  The
second and third hypotheses are not consequences of the promoted C-II route
map.  They are stated here to prevent an invalid transfer from a jammed pure-disk
calculation to the general C-II source.  The phase theorem is used here as an
unpromoted Target B dependency; this report does not promote it into the Target
C route map.

In the source-carrying case, the Target B jammed hypothesis is not an additional
local assumption: a relative-interior C-II stress has positive coefficient on
every contact, and equilibrium at a core hull vertex forces that vertex to be an
endpoint of a positive diameter reaction.  The positive-stress first-variation
identity therefore gives the required pinned expansive-cone condition.  With
isolates present, this argument applies only to the core and the phase transfer
is kept explicit in Section 5.

## 2. Contact and population identities

For a simply connected pure rhombic disk, let (R) denote the number of bounded
rhombi.  Every rhombus contributes two train incidences and every train is a
boundary-to-boundary path.  The standard disk Euler identities for the core are

```math
v=R+T+1,
\qquad
e=2R+T.
\tag{PR.2}
```

For completeness, the second identity follows by counting face-edge incidences.
If (B=2T) is the boundary-edge count, then
```math
4R=2e-B,
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
so (e=2R+T).  Euler's formula (v-e+R=1) then gives
\(v=R+T+1).
```



The post-ZF mixed-rigidity quantity is

```math
s_Z=e+h-(2v-2)\ge0.
\tag{PR.3}
```

Substituting (PR.2) gives the exact identity

```math
\begin{aligned}
s_Z
  &=(2R+T)+h-2(R+T+1)+2\\
  &=h-T.
\end{aligned}
\tag{PR.4}
```

Hence every such C-II source satisfies

```math
h\ge T.
\tag{PR.5}
```

No (s_Z=0) assumption has been made; positive surplus makes the inequality
stronger.

If (z) contact-isolated source points are present, (v=n-z), but (PR.2)--
(PR.5) are unchanged because (s_Z) is defined using the nonisolated core.

## 3. Diameter endpoints give the opposing inequality

Every endpoint of a diameter pair is a vertex of the convex hull of (A): if an
endpoint were a nontrivial convex combination of other source points, equality in
the triangle inequality for its distance to the opposite diameter endpoint would
force all participating points to coincide in the same direction at distance
(D), which is impossible for distinct source points.  Therefore all endpoints of
the (h) actual diameter pairs lie among the (q) convex-hull vertices.  We also
use the classical Hopf--Pannwitz/Sutherland--Erdős diameter-graph bound: the
straight-line diameter graph of a finite planar point set has at most as many
edges as vertices.  Applied to the subset of core hull vertices supporting H,
it gives

```math
h=|E(H)|\le |V(H)|\le q.
\tag{PR.6a}
```

Consequently

```math
h\le q.
\tag{PR.6}
```

This step does not assume that every hull vertex is diametral and does not impose
hull saturation together with the secondary diameter-pair minimization.

## 4. Phase contradiction

Apply (PR.1). Since

```math
0.9039456812<1,
```

there are constants (eta>0) and (D_0) such that for every member of a
sufficiently large pure-disk sequence,

```math
q\le(1-\eta)T<T.
\tag{PR.7}
```

Combining (PR.5), (PR.6), and (PR.7) yields

```math
T\le h\le q<T,
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
which is impossible.  Thus no sufficiently large C-II global minimizer can lie
in the exact pure simply connected rhombic-disk subbranch described in Section 1.
\(□\)
```



## 5. Why the phase estimate still applies with (O(D)) isolates

This subsection records the only population transfer used in the preceding
extension.  It is not an assertion for a superlinear isolate population.

The standard lattice comparison for the global minimum gives

```math
\frac{n}{D^2}\longrightarrow \Delta_2:=\frac{\pi}{2\sqrt3}.
\tag{PR.8}
```

If (z=O(D)), then the sharper density comparison gives

```math
v=\Delta_2D^2+O(D).
\tag{PR.8a}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
In the C-II pure-core branch,
(PR.5) and (PR.6), together with the convex-hull diameter bound
\(q\le\pi D+O(1)), give
```



```math
T\le h\le q\le\pi D+O(1).
\tag{PR.9}
```

Therefore (T=O(D)), and the core Euler identity gives

```math
\frac{R}{D^2}=\frac{v-T-1}{D^2}\longrightarrow\Delta_2,
\qquad R=\Delta_2D^2+O(D).
\tag{PR.10}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The rhombi have disjoint interiors and each has area at least
\(a_0=\sqrt3/2\), while the core diameter is (D) by the explicit hypothesis.
Hence
```



```math
a_0R\le \operatorname{area}\operatorname{conv}V(G_C)\le\frac{\pi D^2}{4},
```

and (PR.10) make both inequalities asymptotic equalities with an (O(D))
area error.  In particular the total angular rhombus defect is (O(D)), the
same input used in the atomic phase proof.  The normalized core hulls converge
to the unit-diameter disk.  These are precisely the dense-area, (T=\Theta(D)),
disk-limit, and (O(D))-defect inputs used in the audited Target B
phase/exposed-hull proof of (PR.1); no independently selected scaffold is
introduced.  The train graph is the actual train graph of (G_C), and (q) is
its actual core hull-vertex count.

Thus the pure-disk phase estimate is stable under (O(D))
contact-isolated points.  The argument fails for a superlinear isolate
population because the core may lose the (O(D)) area/defect budget even though
it still has the same limiting density.

## 6. Why this does not close C-II

The proof uses the exact identity (s_Z=h-T), so it is valid for all three
values of (s_Z) *within this subbranch*.  It also uses no assumption that the
diameter graph is cyclic or a forest, and it retains the actual (h), not merely
the number of loaded vertices.

The missing implication is the topology/population upgrade:

```math
\text{C-II + global optimality}
\quad\Longrightarrow\quad
\text{an exact simply connected pure rhombic contact core with }z=O(D).
\tag{PR.11}
```

The current promoted stack does not prove (PR.11).  Its almost-rhombic theorem
allows (O(D)) boundary/nonquadrilateral/outer-walk defects, holes, components,
and contact-isolated source points.  The full-source transport theorem also
retains these terms rather than deleting them.  In particular, one cannot replace
the exact identity (PR.4) by (s_Z=h-T+O(D)) and then use (PR.1): the unknown
defect term is of the same order as the phase gap.

Likewise, the strict-rattler absorption result supplies a same-(D) minimizer with
no contact-isolated points, but it may create new contacts and therefore does not
preserve the contact-minimal C-II normalization.  It cannot be used to establish
(PR.11).

## 7. Regression audit

- **Odd shells:** they are not exact simply connected pure rhombic disks carrying
  the source in the sense of Section 1; their (s_Z=2) does not invalidate the
  algebra, but they remain outside the phase theorem's exact hypotheses.
- **Holes/components:** excluded explicitly by hypothesis; no hole is silently
  absorbed into Euler's formula.
- **Exceptional faces:** excluded explicitly; the proof does not treat an
  exceptional face as a rhombus.
- **Repeated outer-walk edges:** absent in a topological disk with the stated
  pure-complex hypotheses; no boundary walk is used as though it were simple in
  the general branch.
- **Contact-isolated sources:** (O(D)) isolates are covered by Section 5;
  a superlinear isolate population is not.
- **Diameter endpoints:** only the one-way implication “diameter endpoint implies
  hull vertex” is used.

The result is therefore a genuine exact subbranch exclusion, not a proof that the
remaining almost-rhombic C-II branches are impossible.
