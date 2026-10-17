> Generated reading edition · [exact source](../../../docs/audits/target_c_inactive_diameter_cubic_budget_independent_audit_2026-10-08.md) · source SHA-256 `fd822a57b6de15ace8513babbe694cfa253d88bacff8bcd6b9e3feb37402ac8e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B41BD5D0BEC7","canonical":true,"claim_ids":["C-GLOBAL-NEAR-DIAMETER-PHASE-PURITY","C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET","C-INACTIVE-NEAR-DIAMETER-DEGREE-REGRESSION","C-INVERSE-D-SCALE-PACKET-MATCHING"],"claim_statuses":{"C-GLOBAL-NEAR-DIAMETER-PHASE-PURITY":"canonical","C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET":"canonical","C-INACTIVE-NEAR-DIAMETER-DEGREE-REGRESSION":"regression","C-INVERSE-D-SCALE-PACKET-MATCHING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit of PR #664: inactive inverse-D cubic budget

Date: 2026-10-08. Audit base: `edfceba1fa7743332071c0825660de0654113b6f`, state `2026-10-08.audit.125`. Target C C-II remains open.

Frozen source: PR #664, branch `swarm/sol/inactive-diameter-cubic-moment-20261004`, tip `e62f84e51590fa2660439ea0a2374e4a19e94c5c`. Source report SHA-256 `cec18bd5167f82f513274345262309c11b45f7139ee2892f7d0b228909e42c19`; verifier SHA-256 `0aaa48bcfda8e03cfb6fb156906fc6c8082dc6df505d81404d508d3d388761aa`.

## Verdicts

- **PASS — promote `C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET`.** The finite deficit-weighted cubic moment survives independent reconstruction for every finite planar unit-separated source under its stated diameter threshold. The global-minimizer truncation uses only canonical `C-FS-GEOM`.
- **PASS — promote `C-INVERSE-D-SCALE-PACKET-MATCHING`.** The matching consequence follows for arbitrary near-diameter subgraphs, and the owned bipartite packet corollary follows with the stated one-pair-per-owner condition. The separate near-unit matching bound is also valid when `D>=10c`.
- **PASS — promote `C-GLOBAL-NEAR-DIAMETER-PHASE-PURITY`.** The bound holds for every vertex with at least two near-diameter neighbors; it excludes any fixed positive angular span for sufficiently large global-minimum sources.
- **REGRESSION VALID — promote `C-INACTIVE-NEAR-DIAMETER-DEGREE-REGRESSION`.** Exact nonglobal rational sources have a root with one actual diameter neighbor but linearly many inverse-D near-diameter neighbors. This refutes transferring actual-diameter star bounds to all near-diameter pairs.
- **CONDITIONAL ONLY — do not promote the THIN synchronized-row application or its packet hypotheses.** Equations (22) and the crossing/staircase upgrade depend on a proof-only packet theorem and additional unpromoted thinning inputs. None is needed for the source-wide claims above.
- **No frontier change.** The new bounds do not produce a unit triangle or a same-cardinality strict sub-D competitor. C-II and Level I remain open.

## 1. Exact scope and dependencies

For a finite planar unit-separated set A of diameter D, let K=conv(A),
$`\delta_K=\pi D^2/4-\operatorname{area}K`$, and let $`H_c`$ join every pair
of source points at distance at least $`D-c/D`$, whether or not the pair is
an actual diameter. For fixed c>0 and
$`D\ge\max\{2,4\sqrt c,2c\}`$, put
```math
B_c=1+\lceil20\sqrt c\rceil,\qquad M_c=2(4\sqrt c+1)^2.
```
The finite claim is
```math
\sum_{v:d_c(v)>B_c}(d_c(v)-1)^3\le3072M_cD\delta_K.
```
For a noncollinear global minimum-diameter source, canonical `C-FS-GEOM` gives
$`\delta_K<\pi\sqrt3D/4`$, and hence
```math
\sum_v(d_c(v)-B_c)_+^3<C_cD^2,\qquad C_c=768\pi\sqrt3M_c.
```
No source vertex, including a contact-isolated vertex, is removed. The finite
inequality is independent of C-II; only its global-minimum corollary uses
`C-FS-GEOM`.

## 2. Independent reconstruction of the finite energy bound

### Constant-width completion and regularity

A compact convex K of diameter D is contained in a maximal compact convex
body W of diameter at most D: the family is nonempty, lies in a fixed D-ball,
and the closure of the union of a chain is a compact convex upper bound. A
maximal member has nonempty planar interior, since a segment or point can be
enlarged by a sufficiently small off-line point without exceeding D. If a
boundary point x of W had no diametral partner, compactness would give
$`\max_{y\in W}|x-y|<D`$. Choose a direction pointing outside W and move x a
sufficiently small positive distance in that direction. Its distances to W
remain below D, so the convex hull with the moved point still has diameter at
most D, contradicting maximality. Every boundary point of W therefore lies
on a diameter. The planar characterization in KMW, introduction and
Proposition 1.3 ([original paper](https://emis.de/ft/11518)), implies W has
constant width D. This independently verifies
the completion step; it does not invoke KMW Theorem 0.1 as an arbitrary-set
completion theorem. KMW Theorem 0.1 itself assumes a Hamiltonian diameter
graph; the proof of its converse explicitly cites Eggleston for the general
completion fact.

Write h for the support function of W and $`\rho=h+h''`$ for its curvature
measure. Constant width gives, distributionally,
$`\rho(\theta)+\rho(\theta+\pi)=D\,d\theta`$. Since both measures are
nonnegative, $`0\le\rho\le D\,d\theta`$. Thus $`h''=\rho-h`$ is bounded,
so $`h\in W^{2,\infty}`$ and W has a unique support point in each normal
direction. If $`p=h-D/2`$, then p is antiperiodic and
$`f=p+p''=\rho-D/2`$. The support-area identity is
```math
E(p):=\int_0^{2\pi}(p'^2-p^2)=2\delta_W,
\qquad \delta_W=\pi D^2/4-\operatorname{area}W\le\delta_K.
```
On antiperiodic H1 functions, E is positive semidefinite: its Fourier modes
have odd integer frequencies and eigenvalues $`j^2-1\ge0`$. Polarization
and semidefinite Cauchy--Schwarz give
```math
E(p,g)=-\langle f,g\rangle,\qquad
|\langle f,g\rangle|^2\le2\delta_K E(g).
```
Translation first harmonics are in the kernel and do not affect this
inequality.

### Angular span and bounded overlap

Let $`\epsilon=c/D`$, and take a vertex v with d=d_c(v) near-diameter
neighbors q. For each q, set $`r=|v-q|`$ and $`n=(v-q)/r`$. Since q is in
W and W has width D,
```math
0\le h(n)-v\cdot n\le D-r\le\epsilon.
```
For any two such neighbors, $`|q-q'|\le D`$ implies
```math
\cos\alpha\ge1-\frac{D^2}{2(D-\epsilon)^2}>0,
```
so their rays occupy a single interval of span $`\theta_v<\pi/2`$. Let its
half-span be a. Sublinearity of h, writing an intermediate unit normal as a
positive linear combination of the endpoint normals, gives
```math
0\le y_v(t):=h(t)-v\cdot n(t)\le\epsilon\frac{\cos t}{\cos a}\le2\epsilon.
```
Distinct source neighbors are unit-separated, while their radii differ by at
most epsilon. Therefore
```math
1\le |q-q'|^2\le\epsilon^2+4D^2\sin^2(\alpha/2),
```
which gives each consecutive ray gap greater than $`1/(2D)`$, and hence
$`\theta_v>(d-1)/(2D)`$.

For any normal in the interval, v lies in the support cap of height
$`2\epsilon`$. If z(n) is the unique support point, write
$`v=z(n)-tn+sJn`$, where $`0\le t\le2\epsilon`$. The opposite support
point is z(-n)=z(n)-Dn. Since diam(W)=D,
```math
(D-t)^2+s^2\le D^2,\qquad |v-z(n)|^2=t^2+s^2\le2Dt\le4c.
```
Each such cap therefore contains at most $`(4\sqrt c+1)^2`$ unit-separated
source points by packing disjoint radius-1/2 disks into a radius-
$`(2\sqrt c+1/2)`$ disk. For the paired intervals $`I_v\cup(I_v+\pi)`$,
the two oriented caps give essential overlap multiplicity at most M_c. This
explicit factor of two pays for antipodal intervals; disjoint-star intervals
are not assumed.

### Curvature payment and cubic moment

For the interval centered at zero with half-width a, define
```math
g_v(t)=\frac{\cos t}{\cos a}-1\quad (|t|\le a),
```
use its negative on the antipodal interval, and set it to zero elsewhere.
This is antiperiodic and belongs to H1. With $`k=\tan a-a`$, direct
integration gives
```math
E(g_v)=4k,\qquad \int(g_v')^2=2(a\sec^2a-\tan a)\le8k,
\qquad k\ge a^3/3.
```
For the middle inequality, put t=tan(a)≤1; the required remainder is
$`5t-(t^2+5)\arctan t`$, whose derivative is at least
$`2t^2(1-t^2)/(1+t^2)\ge0`$.

On the non-antipodal interval, $`y_v+y_v''=\rho`$ and
$`g_v''+g_v=-1`$. Integration by parts, using the actual endpoint-neighbor
slack at most epsilon, yields
```math
\int_{I_v}\rho g_v
=\tan a\,[y_v(-a)+y_v(a)]-\int_{I_v}y_v
\le2\epsilon\tan a.
```
Since $`\tan a\le2a`$, antiperiodicity gives
```math
-\langle f,g_v\rangle\ge2Dk-8\epsilon a.
```
If v is heavy, d>B_c, then $`a>5\sqrt c/D`$, so
$`a^2>24\epsilon/D`$ and $`Dk\ge8\epsilon a`$. Consequently
$`-\langle f,g_v\rangle\ge Dk`$.

Sum $`g_v`$ over heavy vertices and set $`S=\sum k_v`$. Cauchy--Schwarz
pointwise with the M_c overlap bound gives
```math
E(g)\le\int(g')^2\le8M_cS.
```
Also $`-E(p,g)=\langle f,g\rangle\le-DS`$, so semidefinite
Cauchy--Schwarz yields $`D^2S^2\le16M_c\delta_KS`$. If S>0,
$`S\le16M_c\delta_K/D^2`$; for S=0 the result is immediate. Since
$`k_v\ge(d_c(v)-1)^3/(192D^3)`$, the finite cubic inequality follows with
constant 3072M_c. This reconstruction pays the curvature error explicitly;
near-unit pairs do not supply exact KKT contacts or zero curvature.

## 3. Global matching and phase-purity deductions

From the finite inequality and `C-FS-GEOM`, each global source satisfies
$`\sum_v(d_c(v)-B_c)_+^3<C_cD^2`$. For a subgraph F of H_c and any vertex
cover U of size r,
```math
|E(F)|\le\sum_{v\in U}d_c(v)
\le B_cr+C_c^{1/3}r^{2/3}D^{2/3}
```
by Holder. Endpoints of a maximum matching form a cover with r=2\nu(F).
If $`|E(F_D)|\ge(\kappa-o(1))D`$, divide by D along any subsequence on
which $`\nu(F_D)/\sqrt D`$ has a finite limit. This gives
```math
\liminf\frac{\nu(F_D)}{\sqrt D}
\ge\frac{\kappa^{3/2}}{2\sqrt{C_c}}.
```
If an owned bipartite packet has distinct owners, exactly one selected pair
per owner, and partners on the opposite shore, the distinct partner set is a
vertex cover. Selecting one pair per partner is then a matching, so the
partner count has the stronger lower constant $`\kappa^{3/2}/\sqrt{C_c}`$.

For the separate near-unit graph (pairs of length at most $`1+c/D`$), if
D>=10c then seven neighbors of one vertex would contain two consecutive rays
with gap at most $`2\pi/7`$. Their squared separation is at most
$`1/100+4(11/10)^2(22/49)^2<1`$, contradicting unit separation. Thus its
maximum degree is at most six, and every m-edge subgraph has matching number
at least m/12 by taking the endpoints of a maximum matching as a vertex cover.

For phase purity, if $`\theta_v^2\ge96\epsilon/D`$, then
$`a^2\ge24\epsilon/D`$, so the same one-vertex energy estimate gives
$`-\langle f,g_v\rangle\ge Dk_v`$. Applying semidefinite
Cauchy--Schwarz to g_v alone yields
$`D^2k_v^2\le8\delta_Kk_v`$, and $`k_v\ge\theta_v^3/24`$. Otherwise
$`\theta_v<\sqrt{96c}/D`$. Hence every vertex with at least two H_c
neighbors obeys
```math
\theta_v\le\max\left\{\frac{\sqrt{96c}}D,
\left(\frac{192\delta_K}{D^2}\right)^{1/3}\right\}.
```
For a noncollinear global minimizer, canonical `C-FS-GEOM` makes this uniformly
$`\max\{\sqrt{96c}/D,(48\pi\sqrt3/D)^{1/3}\}=o(1)`$.

## 4. Exact inactive-star regression

For every integer D>=64 let m=floor(D/5), include the origin and p=(D,0),
and for each integer i with 0<|i|<=m include
```math
r=D-\frac1{2D},\qquad
q_i=r\left(\frac{1-(i/D)^2}{1+(i/D)^2},
\frac{2i/D}{1+(i/D)^2}\right).
```
All coordinates are rational. Writing $`\theta_i=2\arctan(i/D)`$,
consecutive angular gaps among the q_i are at least
$`2\arctan(25/(26D))`$, so their chord distance exceeds one for D>=64;
their full angular span is below $`2\arctan(1/5)`$. Also
```math
|q_i-p|^2\ge (D-r)^2+\frac{4Dr}{D^2+1}>1,
```
and $`|q_i|=r>1`$. Also $`\cos\theta_i\ge12/13`$, so
$`|q_i-p|^2\le D^2+r^2-2Dr(12/13)<D^2`$; every q_i-q_j chord is at
most $`2r\sin(\arctan(1/5))<D`$. Thus the origin-p pair is the unique
actual diameter edge at the origin. Since $` |\tan\theta_i|\le5/12<1/2`$,
all q_i lie in the triangle with vertices (0,0) and (D,±D/2), giving
$`\delta_K\ge(\pi/4-1/2)D^2`$. Yet
$`d_1(0)=2m+1`$, since every listed partner is at least D-1/D away.
The n=2m+2 point source is nonglobal: a collinear n-point unit-separated
competitor has diameter n-1=2m+1<D. Thus a linear inverse-D near-star need
not have multiple actual diameter edges. The verifier checks D=64,128,256;
the stated all-D family is certified by the displayed analytic inequalities.
This regression does not refute any global-minimizer theorem.

## 5. Certificate boundary and excluded applications

The frozen verifier was copied byte-for-byte and passed: 3 rational nonglobal
sources, 7,007 exact source-pair checks, 176 inactive root pairs, 647
rational algebra checks, all 1,100 simple graphs through five vertices,
39,675 cover checks, and 3,300 matching checks. These computations validate
only those finite fixtures and sampled algebra/graph reductions. They do not
certify the constant-width completion, support-energy inequalities, the
unbounded family, global optimality, the analytic cubic bound, or the THIN
packet extraction. Those were audited analytically above.

The source's Section 7 synchronized THIN-row application remains conditional
on an unpromoted packet theorem, and its later crossing/staircase step also
uses unpromoted thinning inputs. Those premises and applications receive no
canonical status. No live discovery branch was modified.
