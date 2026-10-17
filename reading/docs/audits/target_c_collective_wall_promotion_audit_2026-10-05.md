> Generated reading edition · [exact source](../../../docs/audits/target_c_collective_wall_promotion_audit_2026-10-05.md) · source SHA-256 `b6fe584d9c88046458fd31e5b07031958a0a960b88ba72679106794b5f701791`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D16153EED6A6","canonical":true,"claim_ids":["C-EMBEDDED-WALL-REFILL","C-FIXED-WALL-ACTIVATION-REGRESSION","C-LARGE-WALL-LOCK-REGRESSION","C-PENTAGON-WALL-DISJOINT-BULK"],"claim_statuses":{"C-EMBEDDED-WALL-REFILL":"canonical","C-FIXED-WALL-ACTIVATION-REGRESSION":"regression","C-LARGE-WALL-LOCK-REGRESSION":"regression","C-PENTAGON-WALL-DISJOINT-BULK":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent promotion audit — Target C embedded refill and collective pentagon-wall bulk

**Date:** 2026-10-05  
**Audit base:** \`fd81b486e90a509c2c1bee1373676f4f660148ee\`  
**Starting theorem state:** \`2026-10-05.audit.53\`  
**Target:** C-II / source replacement and collective-wall frontier  
**Verdict:** **PASS for two canonical claims and two binding regressions.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes:

1. \`C-EMBEDDED-WALL-REFILL\` — canonical;
2. \`C-PENTAGON-WALL-DISJOINT-BULK\` — canonical;

and registers:

3. \`C-FIXED-WALL-ACTIVATION-REGRESSION\` — regression;
4. \`C-LARGE-WALL-LOCK-REGRESSION\` — regression.

The positive theorems materially advance the current active-diameter frontier. The regressions deliberately block a false converse: positive Oler residual, phase frustration, or even a very large near-triangular unit wall is not itself a certificate of fixed-wall spare capacity.

## 1. Embedded contact walls give exact full-source replacement contracts

Audited source:
\`docs/reports/target_c_embedded_grain_wall_replacement_2026-10-02.md\`.

Let $`C`$ be a simple polygonal wall made of actual unit contacts in the original source, with $`C\subset K=\operatorname{conv}A`$. Define
```math
W_C=
\{x\in\operatorname{int}C:\ |x-b|>1\ \text{for every wall vertex }b\}.
```

### 1.1 Wall shield

For $`x\in W_C`$ and any old source point $`q\notin\operatorname{int}C`$, $`q`$ not a wall vertex, follow the segment $`[x,q]`$ to its first wall intersection $`z`$.

If $`z`$ is a wall vertex, then
```math
|x-q|=|x-z|+|z-q|>2.
```

If $`z=(1-t)a+tb`$ lies inside a unit wall edge $`ab`$, then the weighted-square identity gives
```math
|x-z|^2
=(1-t)|x-a|^2+t|x-b|^2-t(1-t)
>1-t(1-t)\ge\frac34,
```
while original unit separation gives
```math
|q-z|^2
\ge1-t(1-t)\ge\frac34.
```
Hence
```math
\boxed{|x-q|>\sqrt3.}
```

Thus every point of $`W_C`$ is strictly unit-clear from every retained old point outside the wall.

The same crossing proof yields joint compatibility for finitely many wall packets with pairwise disjoint interiors. If $`Y_j\subset W_{C_j}`$ are individually unit-separated, then every point chosen in one packet is strictly more than one from every point chosen in another packet.

No contact isolate is deleted or ignored; outside isolates satisfy the same shield.

### 1.2 Contact-minimal refill

Let $`S=A\cap\operatorname{int}C`$. Suppose there is a finite unit-separated set $`B\subset W_C`$ with
```math
|B|\ge|S|,
```
and at least one point of $`S`$ is contact-nonisolated.

Because $`W_C`$ is open and $`B`$ is finite, a sufficiently small common dilation of $`B`$ stays in $`W_C`$ while making every mutual distance strictly greater than one. Replace $`S`$ by exactly $`|S|`$ of these strict sites.

All new-old lower constraints are strict by the wall shield; all new-new lower constraints are strict by dilation. Every new point lies in $`\operatorname{int}K`$, so every pair involving a new point has distance strictly below $`D=\operatorname{diam}K`$: if an interior point formed a diameter pair, the segment could be extended a positive amount inside $`K`$ away from its partner, contradicting maximality of $`D`$.

Thus the new source has diameter at most $`D`$, remains triangle-free, and creates no new unit contact. At least one old contact is removed. If the new diameter is below $`D`$, global optimality is contradicted; if it remains $`D`$, contact-minimality among triangle-free minimizers is contradicted.

Therefore a canonical contact-minimal triangle-free minimizer cannot contain such a wall/packet.

### 1.3 Simultaneous strict diameter-cover refill

Now let $`C_j`$ have pairwise disjoint interiors, put $`S_j=A\cap\operatorname{int}C_j`$, and let $`B_j\subset W_{C_j}`$ be certified unit-separated packets of cardinalities $`M_j`$.

Let $`T`$ be a vertex cover of **all actual diameter pairs**. Interior wall populations contain no diameter endpoint, so $`T\cap\bigcup_jS_j=\varnothing`$.

If
```math
\boxed{
\sum_j M_j
\ge
\sum_j|S_j|+|T|,
}
```
delete $`T\cup\bigcup_jS_j`$ and insert exactly the same number of strictified packet sites.

Every old diameter pair loses an endpoint. The remaining old-old pairs are therefore strictly shorter than $`D`$; all new-old and new-new pairs are strictly shorter than $`D`$ by the interior-hull argument. Finiteness gives one positive global margin:
```math
\boxed{\operatorname{diam}A'<D.}
```

This is an actual same-cardinality strict-diameter competitor theorem. It is not merely contact creation.

Canonical Woodall topology gives the immediate cover sizes
```math
\tau(H)=\nu(H)\quad\text{in the forest branch},
\qquad
\tau(H)\le\nu(H)+1\quad\text{in the odd-unicyclic branch}.
```

### 1.4 Consecutive oblique patches

For an actual consecutive affine patch
```math
p_{ij}=p_{00}+iu+jv,
\quad
0\le i\le r,\quad0\le j\le s,
\quad
|u|=|v|=1,\quad |u\cdot v|<\frac12,
```
put $`t=\sin\theta>\sqrt3/2=:a_0`$.

Every point of its closed parallelogram lies within distance $`<1`$ of one grid vertex after rounding both affine coordinates to a nearest cell corner. Hence the patch contains no other source point.

The depth-one wall-safe inner parallelogram has area
```math
|Q_{-1}|
=
(r-2/t)(s-2/t)t
=
rst-2(r+s)+4/t.
```

Averaging translates of the unit triangular lattice, whose fundamental area is $`a_0`$, shows that any open set $`U`$ has a translate containing at least $`|S|`$ lattice sites whenever
```math
|U|/a_0>|S|-1.
```

Substitution yields the exact embedded-patch exclusion
```math
\boxed{
rs(t-a_0)>(2-a_0)(r+s)-4/t,
\qquad
r,s>2/t.
}
```

Under this inequality the canonical contact-minimal source cannot contain the patch.

### 1.5 Exact seven-face square and stable near-square packet

For the $`7\times7`$ unit square patch, the old interior has 36 points. The source report gives an explicit 38-site triangular-lattice packet inside the strict wall-safe region. The verifier checks every pair and wall guard exactly in $`\mathbb Q(\sqrt3)`$, then checks a common dilation.

Consequently:

```math
\boxed{\text{no canonical contact-minimal triangle-free minimizer contains an actual }7\times7\text{ unit square patch}.}
```

The two spare sites can instead pay diameter-cover deletions in the simultaneous theorem.

The same packet survives any actual $`8\times8`$ point patch whose vertices remain within $`1/50`$ of the ideal square positions while all horizontal/vertical grid-neighbor edges remain unit contacts. The wall stays simple, winding number keeps every packet site inside, and the exact wall-distance margin survives the perturbation.

The certificate rerun passed:

- all 38 exact strict sites;
- strict wall squared margin $`>1/20`$;
- the exact contact reduction $`112\to28`$;
- an explicit $`98\to85`$ squared-diameter competitor;
- simultaneous adjacent-wall packets;
- all four exact oblique area thresholds;
- the stable near-square perturbation packets.

**Verdict:** canonical-ready.

## 2. Quadratic pentagon-to-pentagon train bulk can be made wall-disjoint

Audited source:
\`docs/reports/target_c_pentagon_terminal_wall_disjoint_quadratic_bulk_2026-10-05.md\`.

Let $`\mathcal P`$ be any family of complete actual stopped trains whose two terminal occurrences lie on bounded physical unit pentagons. Let $`P=|\mathcal P|`$, and let $`R_{PP}`$ count strict-rhombus crossings between pairs of trains in $`\mathcal P`$.

Put
```math
K=250,
\qquad
c_K=
\frac1{(K+1)^2}
\left(\frac K{K+1}\right)^{2K}>0.
```

### 2.1 Self-overlapping terminal walls cost only bounded crossing mass

If the two terminal pentagons of one train share a source vertex, each terminal edge midpoint lies within Euclidean distance two of that vertex. Their mutual distance is at most four.

The canonical stopped-train monotone projection advances by at least
```math
a_0=\frac{\sqrt3}{2}
```
per crossed strict rhombus. Hence
```math
a_0r_\tau\le4.
```
Since $`5a_0>4`$,
```math
r_\tau\le4.
```

Removing all such trains loses at most $`4P`$ crossing edges.

### 2.2 Terminal-wall conflict degree is uniformly bounded

Triangle-freeness gives contact degree at most five. At one source vertex at most five physical pentagonal face occurrences are incident. Each physical pentagon has five terminal train occurrences. Therefore at most $`25`$ trains can have a terminal pentagon containing a prescribed source vertex.

A train whose two terminal pentagon walls are disjoint uses ten source vertices. Its wall-support conflict degree is therefore at most
```math
K=10\cdot25=250.
```

At most $`KP/2`$ crossing pairs are wall-conflicting.

### 2.3 Probabilistic thinning retains a fixed fraction of all nonconflicting crossings

Choose each remaining train independently with probability
```math
p=\frac1{K+1},
```
and retain it only if none of its wall-conflict neighbors was chosen.

The retained terminal wall supports are pairwise source-vertex-disjoint.

For one nonconflicting crossing pair $`\tau,\sigma`$, simultaneous retention has probability at least
```math
p^2(1-p)^{2K}=c_K.
```

Linearity of expectation gives a retained family $`\mathcal A`$ with
```math
\boxed{
R(\mathcal A)
\ge
c_K
\left[
R_{PP}-(4+K/2)P
\right]_+.
}
```

No independence between different crossing events is required.

Thus if $`P=O(D)`$ and
```math
R_{PP}=(\Delta_2-o(1))D^2,
\qquad
\Delta_2=\frac{\pi}{2\sqrt3},
```
then
```math
R(\mathcal A)\ge(c_K\Delta_2-o(1))D^2.
```

After discarding selected trains with fewer than
```math
\gamma D,
\qquad
\gamma=\frac{c_K\Delta_2}{12\pi},
```
selected crossings, one retains a family $`\mathcal L`$ satisfying
```math
\boxed{
R(\mathcal L)\ge\frac{c_K\Delta_2}{4}D^2,
\qquad
|\mathcal L|\ge\sqrt{c_K\Delta_2}\,D.
}
```

Every $`\tau\in\mathcal L`$ has terminal edge midpoints separated by at least
```math
\boxed{
|x_\tau-y_\tau|
\ge
\rho D,
\qquad
\rho=a_0\gamma>0.
}
```

The midpoint separation is source-space geometry from monotone projection, not reciprocal length.

The exact thinning verifier passed 1,656 Bernoulli outcomes, all 47 nonconflicting crossing-pair probabilities, all support-disjointness checks, the degree-250 conflict bound, and the exact five-rhombus versus four-unit-span inequality.

### 2.4 The low-endpoint-defect application is now independently canonical

The original report cited a proof-only branch note for the pentagon-pair localization. This audit rederives that localization directly from canonical audit.53 inputs.

Let $`G_D`$ be the canonical good-unit-hull train family from \`C-FULLCORE-HULL-DEPLETION-FLOOR\`, and let $`M_D`$ be the trains remaining after deleting $`G_D`$. Canonically,
```math
R_{\rm bulk}
=
(\Delta_2-o(1))D^2,
\qquad
M_D\ge(2s-o(1))D,
\qquad
s=\sqrt{\Delta_2}.
```

Write the occurrence-counted outer contact walk as routes of lengths $`\ell_i`$ between consecutive loaded force-hull vertices. A route is good exactly when $`\ell_i=1`$. If $`m_B`$ is the number of nonunit loaded-hull sides, then
```math
x_B=b-q=\sum_{\ell_i>1}(\ell_i-1).
```
Hence the total bad outer terminal-occurrence capacity is exactly
```math
\boxed{
B_{\rm bad}
=
\sum_{\ell_i>1}\ell_i
=
x_B+m_B
=
2m_B+u_B,
}
```
where $`u_B=x_B-m_B`$.

For bounded exceptional physical faces, with
```math
Q-f=\sum_F(\deg F-5),
```
the total terminal-occurrence capacity on faces of degree at least six is
```math
\sum_{\deg F\ge6}\deg F
\le
6(Q-f),
```
since $`d\le6(d-5)`$ for every integer $`d\ge6`$.

Let $`P_D`$ be the number of the $`M_D`$ retained trains whose **two** terminal occurrences are both on bounded physical pentagons. Every other retained train has at least one terminal occurrence either on a bad outer interval or on a degree-$`\ge6`$ exceptional face. Stopped trains partition terminal occurrences, so different trains can be charged to different chosen occurrences. Therefore, finitely,
```math
\boxed{
M_D-P_D
\le
2m_B+u_B+6(Q-f).
}
```

Thus
```math
P_D+2m_B+u_B+6(Q-f)
\ge
(2s-o(1))D.
```

In particular, if
```math
m_B=o(D),
\qquad
u_B=o(D),
\qquad
Q-f=o(D),
```
then
```math
P_D\ge(2s-o(1))D.
```

Let $`R_{PP}`$ be crossings whose two trains both lie in this pentagon-pair family. Since $`T=O(D)`$, hence $`M_D=O(D)`$, removing the $`o(D)`$ other train vertices destroys only $`o(D^2)`$ crossing edges:
```math
R_{PP}
\ge
R_{\rm bulk}
-
(M_D-P_D)M_D
=
(\Delta_2-o(1))D^2.
```

The finite wall-disjoint theorem now applies. Consequently the low-endpoint-defect branch contains
```math
\boxed{\Omega(D)}
```
complete actual trains, each of source-space length $`\Omega(D)`$, with pairwise source-vertex-disjoint terminal physical pentagon walls, whose crossing graph still contains
```math
\boxed{\Omega(D^2)}
```
actual strict rhombi.

This is new canonical collective source structure. It does **not** by itself supply a simultaneous wall motion or a strict competitor.

**Verdict:** canonical-ready.

## 3. Regression: positive residual does not imply fixed-wall capacity

Audited source:
\`docs/reports/target_c_phase_frustration_fixed_wall_activation_regression_2026-10-05.md\`.

The regular unit pentagon has:

- five exact unit boundary contacts;
- five equal longer diagonals, loading every boundary vertex in the finite KKT packet;
- a positive normalized KKT stress with PSD stress matrix and exactly the three affine kernel modes;
- mixed rigidity;
- strictly positive fixed-boundary Oler residual;
- definite reduced-phase mismatch.

Yet its fixed-wall capacity for even one interior unit-clear point is zero.

Its circumradius satisfies
```math
R^2=\frac{5+\sqrt5}{10}<1.
```
Triangulating the pentagon by its center and splitting each fan triangle by the perpendicular bisector of the unit boundary side shows that every point in the pentagon lies within distance $`<1`$ of a wall vertex.

After deleting **any one** boundary vertex, the convex hull of the remaining four vertices plus the deleted ear is still covered by unit disks centered at the four retained vertices; every point except the deleted vertex itself has distance $`<1`$ from one retained wall point.

Therefore:
```math
\boxed{
\text{positive residual + phase mismatch + positive KKT/mixed rigidity}
\not\Longrightarrow
\text{one fixed-wall spare site},
}
```
even after deleting one wall point.

The exact verifier passed the algebraic contact/diameter distances, positive KKT equilibrium, PSD stress identity, covering-radius inequalities, and positive residual.

The source report additionally attributes the regular pentagon's finite global optimality to Bateman--Erdős; this regression does not need that attribution for the local implication above.

**Verdict:** register as regression.

## 4. Regression: arbitrarily large near-triangular unit walls can still be locked

Audited source:
\`docs/reports/target_c_large_near_triangular_fixed_wall_lock_2026-10-05.md\`.

For $`m,n\ge2`$, let
```math
X_{m,n}(\phi)
=
\{iu+jv_\phi:0\le i\le m,\ 0\le j\le n\},
\quad
v_\phi=(\cos\phi,\sin\phi),
\quad
\frac\pi3<\phi<\frac\pi2.
```

The complete contact graph consists exactly of the horizontal and $`v_\phi`$-direction grid edges and is triangle-free. Unit weights give positive equilibrium at every interior vertex.

Let the full boundary grid be fixed. For any same-cardinality labelled unit-separated alternative with maximum displacement
```math
\rho=\max_{ij}|\delta_{ij}|,
```
summing the original contact lower constraints from both opposite walls gives
```math
-2i\rho^2
\le
u\cdot\delta_{ij}
\le
2(m-i)\rho^2
```
and the analogous $`v_\phi`$-bounds. Resolving in the dual basis yields
```math
|\delta_{ij}|
\le
\frac{2(m+n)}{\sin\phi}\rho^2.
```
Hence
```math
\boxed{
\rho=0
\quad\text{or}\quad
\rho\ge
\frac{\sin\phi}{2(m+n)}
\ge
\frac{\sqrt3}{4(m+n)}.
}
```

At $`\phi=\pi/3`$, the Oler/Groemer equality case already audited in the canonical residual stack makes the prescribed-wall triangular grid the unique full packing in its parallelogram.

Compactness then gives, for every fixed $`m,n`$, a positive angle window
```math
0<\phi-\pi/3<\varepsilon_{m,n}
```
in which the same prescribed wall admits no alternative full packing at all.

Thus arbitrarily large triangle-free near-triangular unit walls can carry quadratic interior population and positive pinned equilibrium while admitting **no** strict fixed-wall same-cardinality refill.

There is also an explicit algebraic family with positive Oler residual below one for which Oler already forbids one additional point in the container, even without retaining the wall.

The exact verifier passed:

- 3,404 exact source-pair constraints in eight $`\mathbb Q(\sqrt3)`$ grids;
- exact triangle-free contact support and positive equilibrium;
- full pinned rank on 82 interior vertices;
- all residual identities and 265 displacement/radius checks;
- 1,444 exact residual floors for the explicit capacity-optimal family.

The compactness window is analytic and intentionally non-effective.

Therefore:
```math
\boxed{
\text{large unit wall + quadratic population + positive equilibrium + near-triangular geometry}
\not\Longrightarrow
\text{strict fixed-wall refill}.
}
```

A successful activation theorem must use additional structure such as actual diameter loading, a movable interface, certified packing surplus, or the collective defects/returns supplied by the current canonical stack.

**Verdict:** register as regression.

## 5. Effect on the live C-II frontier

After audit.54, the active-diameter problem has a more precise positive/negative boundary.

Positive:

- certified wall-safe packing surplus is genuinely spendable;
- enough surplus to pay an actual diameter vertex cover gives a strict same-cardinality sub-$`D`$ source;
- exact $`7\times7`$ square and near-square consecutive contact patches are forbidden in the canonical contact-minimal source;
- in the low $`m_B,u_B,Q-f`$ full-core branch, quadratic train bulk can be thinned to a macroscopic family of macroscopically long trains with pairwise disjoint physical pentagon terminal walls.

Negative:

- positive residual and phase mismatch alone do not give one spare site;
- even arbitrarily large near-triangular fixed walls need not admit any strict refill.

The natural next theorem is therefore **collective movable-wall activation**, not universal fixed-wall capacity: use the disjoint terminal pentagon walls, loaded-return structure, reciprocal train geometry, and exact contact manifold to move or replace many walls together while paying the actual diameter cover.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.54\`, register the two positive claims as canonical, and register the two fixed-wall statements as regressions.
