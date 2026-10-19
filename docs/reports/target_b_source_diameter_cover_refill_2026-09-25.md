<!-- theorem-state: {"artifact_id":"ART-E05ADD8C1525","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cf73d2d0c000f170278351eb806782301d3e6ada", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_b_source_diameter_cover_refill_2026-09-25.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "aa31ca2bb5815bdeadcdd5239cfe31dc74eff9ea319bd013152d13d45c30e3ff"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — source diameter cover and deep-vacancy refill

**Date:** 2026-09-25
**Repository commit:** `15cd5d8a8346b42101b355afebd6da28ccd58886`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof attempt
**Target:** B, with an all-source lemma
**Starting status:** Target B and Level I open
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
**External literature search:** not used
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Canonical endpoint and implication chain

The Target B sufficient closure is
\[
G+E\ge (\sqrt3/4)B+(\sqrt3/2)(t+\chi-1),
\]
while a global minimizer has the strict reverse inequality. The present route instead seeks a same-cardinality source with diameter strictly below \(D\):

```text
source diameter-pair cover + verified deep vacant sites
 -> remove every active diameter pair and refill all removed source points
 -> strict sub-D competitor
 -> eliminate a wide, refillable deep-corridor subbranch of Target B.
```

This does not derive the full shell inequality. In particular, it does not say that an arbitrary pocket supplies vacant sites at unit clearance.

## 2. Finite cover-and-refill theorem

Let \(A\) be **any** finite unit-separated planar set, \(D=\operatorname{diam}A\), and \(K=\operatorname{conv}A\). Let \(V_D\) be the set of endpoints of all pairs in \(A\) at distance \(D\), with \(N=|V_D|\). For a point \(c\in\mathbb R^2\) put
\[
\beta_c=D^{-1}\max_{\{a,b\}\subset A,\ |a-b|=D}|a+b-2c|.
\]
For a line \(\ell\) through \(c\), let \(N_\ell\) be the number of points of \(V_D\) whose distance from \(\ell\) is at most \(\beta_cD\).

**Theorem 2.1 (proved candidate awaiting independent audit).** There is a subset \(S\subset V_D\) meeting every diameter pair and satisfying
\[
|S|\le \left\lfloor\frac{N+N_\ell}{2}\right\rfloor. \tag{2.1}
\]
For any \(\rho>0\), if \(F\subset K_{-\rho}:=\{x:x+\rho\overline B\subset K\}\) is unit-separated, \(\operatorname{dist}(F,A)\ge1\), and \(|F|\ge|S|\), then \(A\) is **not** a global minimum-diameter configuration at its cardinality. More precisely, a subset \(F_0\subset F\) of \(|S|\) sites gives
\[
|(A\setminus S)\cup F_0|=|A|,
\quad\operatorname{sep}((A\setminus S)\cup F_0)\ge1,
\quad\operatorname{diam}((A\setminus S)\cup F_0)<D. \tag{2.2}
\]

**Proof.** Split \(V_D\) into the points in the closed \(\beta_cD\)-strip about \(\ell\) and the points strictly on its two sides. Select every strip point and all points on whichever strict side has fewer members. This gives (2.1). If both endpoints \(a,b\) of a diameter pair are on the same strict side, their signed distances from \(\ell\) are positive with the same sign. Each is then at most the absolute sum of their signed distances, which is at most \(|a+b-2c|\le\beta_cD\), a contradiction. Thus every diameter pair either has a strip endpoint or has endpoints on opposite strict sides; \(S\) meets it.

Every pair of points of \(A\setminus S\) has distance strictly below \(D\), since \(A\) is finite and all its diameter pairs meet \(S\). For \(x\in K_{-\rho}\) and \(y\in K\), choose \(u=(x-y)/|x-y|\) when \(x\ne y\). The inner-parallel condition gives \(u\cdot x\le h_K(u)-\rho\), while \(-u\cdot y\le h_K(-u)\). Consequently
\[
|x-y|\le h_K(u)+h_K(-u)-\rho\le D-\rho. \tag{2.3}
\]
The same argument with both points in \(K_{-\rho}\) gives \(|x-x'|\le D-2\rho\). The stated separation assumptions check every old-old, old-new, and new-new pair. Choosing \(|S|\) sites in \(F\) yields (2.2). \(\square\)

No contact point, including a contact-isolated source point, is silently discarded: only the explicit set \(S\) is removed, and clearance is checked against **all** of \(A\).

## 3. Near-round global-minimizer consequence

**Theorem 3.1 (proved candidate awaiting independent audit).** Suppose \(A_j\) are finite unit-separated sets with diameters \(D_j\to\infty\), and after translations
\[
B(0,(1/2-\eta_j)D_j)\subset K_j\subset
B(0,(1/2+\eta_j)D_j),\qquad \eta_j\to0. \tag{3.1}
\]
There are diameter-pair covers \(S_j\) with
\[
|S_j|\le\tfrac12\operatorname{per}(K_j)+o(D_j)
\le(\pi/2+o(1))D_j. \tag{3.2}
\]
Hence, if for some fixed \(\rho>0\) there are unit-separated sets \(F_j\subset (K_j)_{-\rho}\) with \(\operatorname{dist}(F_j,A_j)\ge1\) and
\[
\liminf_j |F_j|/D_j>\pi/2, \tag{3.3}
\]
then no sufficiently large \(A_j\) is globally minimizing.

**Proof.** All diameter endpoints are vertices of \(K_j\). Indeed, if a diameter endpoint \(a\) were a nontrivial convex combination \(a=tx+(1-t)y\) of distinct \(x,y\in K_j\), strict convexity of squared Euclidean distance to its diametral mate \(b\) would give
\(|a-b|^2<t|x-b|^2+(1-t)|y-b|^2\le D_j^2\), impossible. Distinct consecutive hull vertices are at least one unit apart, so \(N_j\le\operatorname{per}(K_j)\).

Set \(R_j=D_j/2\). For any diameter pair \(a,b\), the parallelogram identity and (3.1) give
\[
|a+b|^2=2|a|^2+2|b|^2-D_j^2
\le4(\eta_j+\eta_j^2)D_j^2. \tag{3.4}
\]
Fix the horizontal line through the origin. We show that the number of hull vertices in the band \(|y|\le t_jD_j\), where \(t_j=2\sqrt{\eta_j+\eta_j^2}\), is \(o(D_j)\). For all sufficiently large \(j\), the right and left portions of \(\partial K_j\) in this band are respectively graphs \(x=x_+(y)\) and \(x=x_-(y)\) over \([-t_jD_j,t_jD_j]\). The first graph is concave and the second convex. Their \(x\)-values lie between the two circles in (3.1): on the right, for example,
\[
\sqrt{(1/2-\eta_j)^2-t_j^2}\,D_j
\le x_+(y)\le(1/2+\eta_j)D_j.
\]
The width of this interval is \(O(\eta_jD_j)\), since \(t_j^2=O(\eta_j)\). A concave function taking values in an interval of width \(w\) has total variation at most \(2w\). The right arc therefore has length at most \(2t_jD_j+O(\eta_jD_j)=o(D_j)\), and likewise the left arc. Each arc contains at most its length plus one unit-separated successive hull vertices. Thus \(N_\ell=o(D_j)\). Apply (2.1), \(N_j\le\operatorname{per}K_j\), and Cauchy's planar perimeter-diameter inequality \(\operatorname{per}K_j\le\pi D_j\). Equation (3.3) then supplies more sites than the cover in (3.2), and Theorem 2.1 gives a strict competitor. \(\square\)

For **actual global minimizers**, (3.1) is canonical: the strict lattice comparison and finite Oler bound make the isodiametric area deficit \(O(D)\); after scaling, every convex limit has diameter one and area \(\pi/4\), hence is the radius-\(1/2\) disk. This is the same near-disk argument used in Target B Section 39. Theorem 3.1 is not restricted to the pure-rhombic or triangle-free branch.

## 4. A concrete corridor criterion

**Corollary 4.1.** Under Theorem 3.1, suppose each \((K_j)_{-\rho}\) contains a rectangle of length \(L_j\) and width at least \((k-1)\sqrt3/2\), where \(k\ge1\) is a fixed integer, \(L_j/D_j\to\lambda>0\), and the whole rectangle is at distance at least one from \(A_j\). If
\[
k\lambda>\pi/2, \tag{4.1}
\]
then no sufficiently large \(A_j\) is globally minimizing.

**Proof.** In the rectangle put \(k\) rows at separation \(\sqrt3/2\), with unit horizontal spacing and alternate horizontal offsets \(0,1/2\). Every row contains at least \(\lfloor L_j\rfloor\) sites. Same-row distances are at least one, adjacent-row distances are at least \(\sqrt{(1/2)^2+(\sqrt3/2)^2}=1\), and nonadjacent-row distances exceed one. The rectangle's clearance checks every source-site pair. Thus there are at least \(k\lfloor L_j\rfloor=(k\lambda-o(1))D_j\) admissible sites. Use (4.1) and Theorem 3.1. \(\square\)

For example, a radial corridor of length \((1/2-\varepsilon)D\) with four refillable triangular rows is excluded whenever \(0<\varepsilon<(4-\pi)/8\). This is a **source-level** strict-diameter conclusion, conditional only on the stated geometric vacancy, not on a scaffold or stress. It does not claim that the canonical phase cut produces such a rectangle.

There is also a useful contrapositive below the four-row threshold. If the rectangles in Corollary 4.1 occur in a sequence of **global** minimizers, (2.1) and their \(k\lfloor L_j\rfloor\) sites force
\[
\liminf_j N_j/D_j\ge 2k\lambda. \tag{4.2}
\]
Indeed, a global minimizer must have strictly fewer admissible sites than the displayed diameter cover, and \(N_{\ell,j}=o(D_j)\). A two-row radial corridor with \(\lambda\to1/2\) would therefore require about \(2D\) actual diametral hull vertices; three rows would require about \(3D\), close to the universal \(\pi D\) upper bound. This is a source-level endpoint count, not a count of train terminals or selected stress edges.

## 5. Hostile scope audit and remaining bridge

### 5.1 Exact staggered-wall regression: deep boundary with no deep vacancy

For integer \(m\ge2\), set
\[
c_m=1/2-m^{-3},\quad s_m=\sqrt{1-c_m^2},\quad
u=(1,0),\quad v=(c_m,s_m).
\]
Let \(L_m=\{iu+jv:i,j\in\mathbb Z,\ j\le0\}\) and
\(U_m=\{(i+1/2,1)+jv:i,j\in\mathbb Z,\ j\ge0\}\), and retain from their union only points in \(B(0,m+3)\); call the resulting finite source \(A_m\). Within each half-lattice, horizontal rows and consecutive vertical rows bound strict unit rhombi of angle \(\arccos(c_m)>\pi/3\). The two wall rows are
\[
\{(i,0):i\in\mathbb Z\},\qquad
\{(i+1/2,1):i\in\mathbb Z\}.
\]

This source is unit-separated and triangle-free. For vectors within one half-lattice, the squared distance is \(i^2+j^2+2c_mij\); its only unit vectors are \(\pm u,\pm v\), since \(c_m<1/2\) makes \(|u-v|>1\), and all other nonzero integer pairs have squared length greater than one. Across the two halves, vertical separation is at least one. At separation exactly one the horizontal difference is half-integral, so the distance is at least \(\sqrt5/2>1\); at larger vertical separation it is already greater than one. No cross-grain contact exists.

Every point of \(B(0,m-3)\) lies at distance **strictly less than one** from \(A_m\). For \(y\le0\) or \(y\ge1\), the point lies in a full half-lattice rhombus. Rounding both rhombus coordinates to the nearest vertex puts it within
\(\tfrac12\max(|u+v|,|u-v|)<1\) of a vertex, and that vertex lies in \(B(0,m+3)\). For \(0<y<1\), use the nearer wall row: its vertical distance is at most \(1/2\), and a wall vertex has horizontal distance at most \(1/2\), so the Euclidean distance is at most \(1/\sqrt2<1\). The wall vertex is also inside the clipping disk. Thus there is **no** unit-clear insertion site anywhere in the entire deep disk \(B(0,m-3)\), although the slit has two boundary chains of length \(\Theta(m)\) inside every fixed inner disk.

The hull is near-round: every point of \(B(0,m-3)\) is within one of \(A_m\), so support functions give \(B(0,m-4)\subset K_m:=\operatorname{conv}A_m\subset B(0,m+3)\). Hence \(D_m=2m+O(1)\). The union of all full strict rhombi contains \(B(0,m-3)\) outside the width-one slit, while \(K_m\subset B(0,m+3)\), so its convexification gap is \(G_m=O(m)=O(D_m)\). There are \(O(m^2)\) rhombi and \(\sin(\arccos c_m)-\sqrt3/2=O(m^{-3})\), so their angular area surplus is \(E_m=O(m^{-1})\). These are exact analytic bounds, with no numerical certificate.

This is a regression to the universal inference
\(Q_\varepsilon=\Theta(D),\ G=O(D),\ E=o(1)\Rightarrow\) linear deep vacancy capacity. It is **not** a canonical jammed pure-rhombic disk: its two grain contact graphs are disconnected, and global optimality is not claimed. A theorem for the canonical source must use its actual connectivity, diameter-pair structure, global optimality, or another condition absent here.

**A contact-bridge variant.** Clip the same two half-lattices at radius \(m\) instead of \(m+3\). For integer \(m\), their leftmost wall points are \(a=(-m,0)\) and \(b=(-m+1/2,1)\). Add
\[
z=a+\left(\frac14-\frac{\sqrt{55}}{10},
           \frac12+\frac{\sqrt{55}}{20}\right).
\]
Direct substitution gives \(|z-a|=|z-b|=1\). Write \(z-a=(z_x,z_y)\); then \(z_x=1/4-\sqrt{55}/10<0\) and \(z_y=1/2+\sqrt{55}/20>1/2\). All other lower-grain points have either \(y\le-s_m\), hence vertical distance \(z_y+s_m>1\), or lie on the wall at \(x\ge-m+1\), hence horizontal distance \(1-z_x>1\). All other upper-grain points lie either on its wall at \(x\ge-m+3/2\), or on rows \(j\ge1\). For \(j=1\), clipping forces \(i\ge-m\), since \(i\le-m-1\) would give \(x\le-m-1/2+c_m<-m\). Hence \(x\ge-m+1/2+c_m\), whose distance from \(z\) is at least \(1/4+c_m+\sqrt{55}/10>1\) for \(m\ge2\). For \(j\ge2\), vertical distance is at least \(1+2s_m-z_y>1\). Thus \(z\) has exactly the two advertised unit contacts and introduces no triangle.

For completeness, each clipped half-lattice contact graph is connected for sufficiently large \(m\). A row at height \(y\) has an integer interval of horizontal indices, centered at a value changing by \(c_m<1/2\) from the next row, with radius \(r(y)=\sqrt{m^2-y^2}\). Every nonextreme row has \(|y|\le m-s_m\) and radius at least \(\sqrt{2ms_m-s_m^2}\), which tends to infinity, so adjacent nonextreme index intervals contain a common integer. At an extreme row, \(|y|\in[m-s_m,m]\); the next row's radius satisfies \(r(|y|-s_m)\ge r(|y|)+c_m\) for all sufficiently large \(m\). Indeed, after squaring, it suffices that \(2ms_m-3s_m^2-2c_m\sqrt{2ms_m}-c_m^2>0\), which holds as \(m\to\infty\). Thus every index at the extreme row also occurs in the next row. Horizontal and \(v\)-edges connect all rows. The added point \(z\) joins the two connected grain graphs. The new source still has no deep unit-clear site and has \(G=O(D),E=o(1)\). Its degree-two bridge point lies outside the rhombic faces, so it remains outside the canonical **pure strict-rhombic disk** hypothesis. Connectivity alone is therefore insufficient; a closing proof must use the stronger canonical face structure or global minimality.

1. **Narrow fjords survive the criterion.** The exact two-row oblique-lattice slit in `target_b_deep_pocket_phase_separator_2026-09-25.md` has linear deep boundary and \(G=O(D),E=o(D)\), but does not provide the four unit-clear rows required by the sample corollary. The present theorem does not contradict that regression.
2. **A pocket is not a site set.** The complement of a rhombus complex can include wall points within unit distance throughout a thin pocket. Measuring its area or boundary alone does not verify the clearance hypothesis \(\operatorname{dist}(F,A)\ge1\).
3. **Near-roundness is used only for the half-perimeter count.** The finite cover-and-refill theorem works for arbitrary source sets and retains all diameter constraints. The implication from a canonical pure-rhombic phase cut to a rectangle meeting Corollary 4.1 is unproved.
4. **Exact objective.** The replacement preserves cardinality and all pairwise unit separations, and its diameter is strictly less than the original, irrespective of whether the replacement contains unit triangles.
5. **Sharp cover scale for arbitrary near-round sources.** Let \(A\) be the vertices of a regular \((2m+1)\)-gon with unit sides. Its diameter graph joins each vertex to its two vertices \(m\) steps away, hence is one odd cycle. Every diameter-pair cover has at least \(m+1\) vertices. Its perimeter is \(2m+1\) and its diameter is asymptotic to \((2m+1)/\pi\), so the minimum cover is \((\pi/2+o(1))D\). The leading constant in (3.2) cannot be lowered using near-roundness and unit separation alone. These polygons are not claimed to be global minimizers.

The exact remaining Target B bridge is: show that every canonical multi-grain survivor whose physical cut has a macroscopic deep boundary either has a refillable deep site set exceeding its diameter-pair cover as in Theorem 2.1, or pays the full joint shell inequality. The two-cell slit shows that no statement based on \(G=O(D)\) and \(E=o(D)\) alone can supply the refillable sites. Dominant-grain transfer and the other Target B branches remain open.

## 6. Claim audit

| Claim | Classification | Dependencies / limit |
| --- | --- | --- |
| Finite cover-and-refill Theorem 2.1 | proved candidate awaiting independent audit | elementary convex support and exact source constraints; no global premise |
| Near-round half-perimeter Theorem 3.1 | proved candidate awaiting independent audit | Theorem 2.1, convex-arc estimate, Cauchy perimeter bound |
| Corridor Corollary 4.1 | proved candidate awaiting independent audit | Theorem 3.1, explicit triangular rows |
| Diametral endpoint floor (4.2) | proved candidate awaiting independent audit | Contrapositive of Theorem 2.1 for a global minimizer |
| Staggered-wall deep-vacancy obstruction | regression | Explicit two-grain source in Section 5.1; contact-connected variant has a degree-two bridge defect, and neither version is certified globally optimal or a pure rhombic disk |
| Near-roundness of global minimizers | canonical input | Target B `01-jammed-rhombic-branch.md`, Sections 24 and 39 |
| General multi-grain or Level I closure | open | No guaranteed deep site set or shell payment |

No theorem-state promotion is requested here. The report is noncanonical until independent audit and the repository promotion transaction.
