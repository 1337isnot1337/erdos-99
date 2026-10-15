<!-- theorem-state: {"artifact_id":"ART-57862741A3FD","canonical":false,"claim_ids":["C-CIRCUMCIRCLE-CENTERED-DISK-CAP-SHARPNESS-REGRESSION","C-FAN-PATH-COMMON-TRUNK-REGRESSION"],"claim_statuses":{"C-CIRCUMCIRCLE-CENTERED-DISK-CAP-SHARPNESS-REGRESSION":"regression","C-FAN-PATH-COMMON-TRUNK-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent Audit.168: cap sharpness and common-trunk fan congestion

- **Date:** 2026-10-08
- **Audit base:** `origin/main=63aff94abedd591fa238c96c997bb0bc63eba4f5`, state `2026-10-08.audit.163`.
- **Frozen source:** `origin/research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`.
- **Source report:** `docs/reports/target_c_sharp_cap_closure_and_unbounded_path_congestion_2026-10-08.md`, SHA-256 `a4987d52b921f175ba2e270f889d41634f9ba910a24a9ef910a13fe62e6bcbba`.
- **Source verifier:** `research/verify_target_c_cap_closure_path_congestion_2026_10_08.py`, SHA-256 `f157c6d502b796c0bb3f7d41b153a44e2e46737acba7dcafa3ef7a33b9520d20`.
- **Verdict:** PASS — the cap lemma and finite closure are already subsumed by Audit.166; REGRESSION VALID — promote the sharp leading cap coefficient and the all-order common-trunk congestion family.
- **Frontier:** unchanged. C-II and Level I remain open.

This audit is against the immutable source snapshot above. It does not use later branch commits. The source branch and all discovery branches were left untouched. Audit.167's protected and post-main workflows both completed successfully before this audit integration began.

## 1. Exact dispositions

| Source claim | Independent verdict | Canonical disposition |
| --- | --- | --- |
| The centered-disk cap threshold and its full-source finite closure (report Sections 2–3) | PASS — already subsumed | No new theorem ID. Audit.166's `C-CIRCUMCIRCLE-UPPER-PAIR-SAFETY` and `C-CIRCUMCIRCLE-BLOCKER-CLOSURE` apply with the disk centered at the carrier and are stronger in canonical sources. |
| Leading coefficient `1-sqrt(3)/2` in that centered-disk threshold | REGRESSION VALID | Register `C-CIRCUMCIRCLE-CENTERED-DISK-CAP-SHARPNESS-REGRESSION`. |
| An unbounded number of fan roots with unique long blocker paths sharing one isolate trunk | REGRESSION VALID | Register `C-FAN-PATH-COMMON-TRUNK-REGRESSION`, including the leading-density augmentation. |

The new family is finite, nonglobal, and has no normalized nonnegative KKT diameter stress. It refutes deductions from the listed source geometry, path lengths, and leading density alone. It does not refute a claim that also uses canonical global optimality or the canonical stress hypotheses.

## 2. Cap lemma: exact overlap and valid sharpness regression

For a source contained in the disk `B(a,D)`, take `c=a`, `R=D`, and the actual diameter pair `p-a`, with `u=(p-a)/D`. In Audit.166's notation,

\[
P=u\cdot(p-c)=D,\qquad E=\sqrt{R^2-D^2/4}=\frac{\sqrt3}{2}D.
\]

For `D >= 10` and `delta <= 1/D`, the large-`E` branch gives

\[
H=P-E-\delta/4=(1-\sqrt3/2)D-\delta/4.
\]

Thus the report's upper-pair lemma is exactly the centered-carrier-disk specialization of `C-CIRCUMCIRCLE-UPPER-PAIR-SAFETY`. Its arrow-closed finite move is the corresponding specialization of `C-CIRCUMCIRCLE-BLOCKER-CLOSURE`; the source report's canonical path conclusion adds no stronger canonical consequence than Audit.166's half-depth theorem.

The new four-point sharpness example is correct. Let

\[
a=(0,0),\quad p=(D,0),\quad
x=(\sqrt3D/2,D/2),\quad y=(\sqrt3D/2,-D/2),\qquad D\ge10.
\]

All four labels are unit-separated. The pairs `ap`, `ax`, `ay`, and `xy` have length `D`, and the other two distances are `D*sqrt(2-sqrt(3)) < D`; hence the actual diameter is `D`. The source is nonglobal, for example by replacing it with four integer-grid points. At `x`, support depth is exactly `(1-sqrt(3)/2)D`. Moving only `x` by `-delta*(1,0)` gives

\[
|x-\delta(1,0)-y|^2=D^2+\delta^2>D^2.
\]

Therefore no uniform leading coefficient greater than `1-sqrt(3)/2` is valid from this diameter-disk geometry alone. This example does not challenge the lower-order `-delta/4` margin in the promoted theorem.

## 3. Independent reconstruction of the all-order source family

Fix an integer `q >= 1`, and put

\[
K=3q,\quad M=64K^2,\quad D=M+\frac1{16M},\quad
\delta=D^{-1},\quad \sigma=\frac1{4M},\quad
w=\frac{1-\sigma^2}{1+\sigma^2},\quad
z=1-\delta^2/2+i\delta w.
\]

The identity `w^2=1-delta^2/4` gives `|z|=1` exactly. Writing `z=e^(i theta)`,

\[
2D\sin(\theta/2)=1,\qquad \delta\le\theta<1.01\delta.
\]

Set `p_j=D*z^j` for `-1 <= j <= K+1`, `a=(0,0)`, `c=1+1/K`, and `rho=1+delta^2/100`. Consecutive wall edges have length exactly one. Add the row

\[
r_j=(D-3+c(D-\Re p_j),\Im p_j),\quad 0\le j\le K.
\]

The `q+1` roots have indices `i=0,3,...,K`. For each root set `u_i=p_i/D`, `f_i=p_i-rho*u_i`, and `v_i=r_i-f_i`. Define

\[
\lambda_i^2=\frac{\rho^2-|v_i|^2/4}{|v_i|^2},\qquad
m_i=\frac{f_i+r_i}{2}+\lambda_i Jv_i.
\]

The actual construction rounds `lambda_i` upward to a rational with denominator `10^6*M^6`. Finally add

\[
t_\ell=(D-3-\ell\rho,0),\quad 1\le\ell\le T=\lceil D/7\rceil.
\]

All coordinates are rational. The label count is (N=8q+7+T<D/5).

### 3.1 Pair graph and nonglobality

The all-`q` bounds used in the pair audit are uniform. Since `D >= 64K^2` and `K >= 3`, all wall angles have magnitude below `0.01`. For `h_j=D*(1-cos(j*theta))`,

\[
0\le h_j\le\frac{1.0201j^2}{2D}<0.008\quad(0\le j\le K),
\]

and the two wall endpoints have `h_-1,h_(K+1) < 0.02`. These give the stated narrow depth and column boxes. In particular, root columns are separated by at least `2.97` in the tangential coordinate before the `0.17` middle-point offsets.

For a row edge, with (A_j=\sin((j-1/2)\theta)), (B_j=\cos((j-1/2)\theta)),

\[
r_j-r_{j-1}=(cA_j,B_j),\qquad
|r_j-r_{j-1}|^2=1+(c^2-1)A_j^2.
\]

It is strictly longer than one and at most `1+delta`. For a connector,

\[
|v_i|^2=(3-\rho)^2+h_i\{-2(3-\rho)A+2\rho^2/D\}
+h_i^2(A^2-\rho^2/D^2),\quad A=c+1-\rho/D.
\]

Here (1.9<A<2.4), (h_i<0.008), and the coefficient of (h_i) is negative. Hence (1.9<|v_i|\le3-\rho<2\rho), so the equal-length midpoint radicand is positive. Its perpendicular offset is below (0.16), since

\[
\rho^2-|v_i|^2/4\le4(\rho-1)+3h_i<0.16^2.
\]

Upward rational rounding changes either segment length by less than (3/(10^6M^6)); the three connector lengths lie in ([\rho,1+\delta^2/50)). The first segment (p_i f_i) has length exactly (\rho).

The complete set of pairs of length at most (1+\delta) is exactly:

1. consecutive wall edges;
2. (p_i f_i), (f_i m_i), and (m_i r_i) for each chosen root;
3. consecutive row edges;
4. (r_0t_1) and consecutive trunk edges.

All listed edges except the wall edges are strict noncontacts. The remaining pair classes are excluded as follows: nonconsecutive wall chords exceed (1.99); for a first-column point and a different wall point,

\[
|f_i-p_j|^2=\rho^2+(1-\rho/D)|p_i-p_j|^2>1.99;
\]

nonmatching middle-to-row pairs have horizontal gap at least (0.96) and tangential gap at least (0.82), hence squared distance above (1.59); nonadjacent row pairs dominate the corresponding nonadjacent wall chord and exceed (1.99); row-to-trunk pairs other than (r_0t_1) have either horizontal gap at least (\rho) plus a nonzero row height, or a horizontal gap above (2\rho); and nonconsecutive trunk pairs exceed (2\rho). The depth and root-column bounds separate the remaining cross-column classes by more than (1+\delta). Thus the full contact graph is exactly the wall path and has no triangle. Every listed row, connector, and trunk point, as well as (a), is contact-isolated.

Every wall point has distance (D) from (a). All other pair distances are strictly below (D): all noncarrier points have horizontal span below (D/6) and vertical span below (2K), so their pairwise distances are (<D) because (D\ge64K^2); the same bounds apply to wall-to-noncarrier pairs. The actual diameter graph is therefore the star from (a) to the (K+3) wall points.

Each (p_i) has exactly two unit contacts (p_{i-1},p_{i+1}), and is an actual degree-one diameter vertex. The triples ({p_{i-1},p_i,p_{i+1}}) are pairwise disjoint because their roots differ by three.

These sources are nonglobal. The verifier constructs (N) separated square-grid points with squared diameter (<2N<D^2). There is also a same-label strict competitor: fix (a), translate every other source point by (-\delta(1,0)), and keep every old pair distance internally unchanged. All carrier distances remain (>1) and become (<D). Since every actual diameter edge at (a) points into the positive first-coordinate half-plane, no normalized nonnegative KKT diameter stress can balance at (a).

### 3.2 Unique arrows and common trunk

For root (p_i), define an arrow (x\to y) when translating (x) by (-\delta u_i) makes an old strict pair have length at most one, or an old contact have length strictly below one. The two wall contacts of (p_i) stay exactly unit under this reflection, while (p_i f_i) becomes shorter than one. The first arrow is therefore the unique strict noncontact (p_i\to f_i).

All three connector arrows and the row-to-trunk/trunk arrows have forward support projection at least (0.9) (at least (0.99\rho) on the trunk). For a row arrow (r_j\to r_{j-1}), (1\le j\le i), its parent-minus-child vector is ((cA_j,B_j)). The angle bounds give

\[
(c^2-1)A_j^2\le\frac52(j-1/2)\delta^2,
\]

\[
2\delta\,u_i\cdot(cA_j,B_j)-\delta^2
\ge(98j/25-99/50)\delta^2.
\]

The second quantity exceeds the first for every (j\ge1), exactly the condition that moving (r_j) makes (r_{j-1}) closer than one. The reverse row, connector, and trunk edges have negative forward projection. Every pair not in the displayed near-unit graph is farther than (1+\delta), so a displacement of length (\delta) cannot make it an arrow. At (r_j), the only outgoing arrow before the threshold is (r_j\to r_{j-1}), and at (r_0) it is (r_0\to t_1). Hence the path

\[
p_i\to f_i\to m_i\to r_i\to r_{i-1}\to\cdots\to r_0\to t_1\to t_2\to\cdots
\]

is unique through its first vertex at support depth

\[
H=(1-\sqrt3/2)D-\delta/4.
\]

For each root,

\[
s_i(t_\ell)=h_i+(3+\ell\rho)\cos(i\theta)
\le3+\ell\rho+0.008.
\]

For (D\ge576), this is (<H) for every (1\le\ell\le\lfloor D/8\rfloor), and (T\ge\lfloor D/8\rfloor). Thus all (q+1) unique paths use the same first \(\lfloor D/8\rfloor\) trunk labels. Each such label is contact-isolated; path congestion is (q+1) on a trunk of length \(\Theta(D)\), while each path reaches at least (D/8) edges before crossing (H).

The path-gap calculation also survives: using (d-1\le(d^2-1)/2), the row part is at most (5K^2/(12D^2)\le5/(768D)), the trunk part is below (2/(700D)+2/(100D^2)), and the three connector edges contribute below (1/(10D^2)). Their sum is (<1/(100D)) for (D\ge576). Small total path excess does not imply path disjointness.

## 4. Leading-density augmentation

This extension is analytic, not a conclusion of the finite verifier. Let (o=(D/2,0)), (R=D/2). Every old point lies in (B(o,R+0.02)). Remove from (B(o,R-3)) all closed radius-((1+\delta)) disks centered at old source points. The remaining region has area

\[
\pi(R-3)^2-N\pi(1+\delta)^2=\pi D^2/4-O(D).
\]

Translate a triangular lattice of systole (1+2\delta) through this region. Averaging over one fundamental cell gives a translation with at least its mean number of sites there, namely

\[
\frac{\pi D^2}{2\sqrt3}+O(D).
\]

The new points have pairwise separation at least (1+2\delta), distance greater than (1+\delta) from every old point, and distance at most (D-2.98) from every old point. They add neither contacts nor blocker arrows, so the graph and unique paths above are unchanged. The full population is (n=\pi D^2/(2\sqrt3)+O(D)). Oler's inequality and \(\operatorname{per}(K)\le\pi D\) give

\[
\operatorname{area}(K)=\pi D^2/4-O(D).
\]

Nonglobality remains explicit. Fix the carrier and all new points, and translate only the original noncarrier labels by (-\delta(1,0)). Original-to-new separation remains (>1), since its old value exceeded (1+\delta). The moved original labels remain within (B(o,R+0.02)), because their first coordinates exceed (5D/6); hence all old-to-new distances remain below (D-2.98). Original internal distances are unchanged, while every carrier diameter shortens. The augmented source is still nonglobal and still has no normalized nonnegative KKT stress.

## 5. Certificate, regressions, and frontier

I inspected the exact rational source construction and the imported `Q(sqrt(3))` comparison helper. The source verifier enumerates all pairs, the complete contact/diameter/near-unit graphs, every outgoing arrow along each path, and an explicit same-cardinality square-grid competitor for (q=1,2,3). It uses `Fraction` throughout the source coordinates and exact quadratic-field signs for the threshold; it contains no floating-point tolerance. I reran it successfully. I additionally called its exact `family(q)` routine for (q=4,5): the largest case has 2,105 source labels, 2,087 contact isolates, 11,625 arrow checks, six fan roots, and 1,800 common trunk labels. These checks corroborate finite instances only; the all-(q) claims above rest on the uniform analytic estimates.

**Promoted regression `C-CIRCUMCIRCLE-CENTERED-DISK-CAP-SHARPNESS-REGRESSION`:** the leading coefficient (1-\sqrt3/2) cannot be increased in the centered radius-(D) disk cap from diameter geometry alone.

**Promoted regression `C-FAN-PATH-COMMON-TRUNK-REGRESSION`:** for every (q\ge1), a triangle-free unit-separated finite source has (q+1) pairwise label-disjoint actual two-contact diameter-fan triples whose unique (1/D)-blocker paths share at least \(\lfloor D/8\rfloor\) contact-isolated labels and have path gap excess (<1/(100D)). The same behavior persists after a leading-density, near-maximal-area augmentation. Every displayed source is nonglobal and has no normalized nonnegative KKT diameter stress. This is not a counterexample to any theorem whose hypotheses require canonical global optimality or canonical KKT stress, and it yields no C-II or Level I conclusion.

The current Target C endpoint remains the source-realized finite move or discrete replacement on the residual face/train system. Audit.166's path theorem still gives no path-disjointness; this exact nonglobal family shows that leading density and small path gap excess alone cannot supply it. No discovery-worker branch was modified.
