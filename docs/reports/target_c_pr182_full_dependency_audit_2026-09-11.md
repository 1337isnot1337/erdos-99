<!-- theorem-state: {"artifact_id":"ART-CA2184B47B89","canonical":true,"claim_ids":["C-PD","C-RSR-DD"],"claim_statuses":{"C-PD":"canonical","C-RSR-DD":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — independent full dependency audit of PR #182

**Date:** 2026-09-11  
**Audited object:** PR #182, `Target C: RSR/DD and boundary-sharing stability raise generic floor above 0.59834`  
**Target:** Target C, post-ZF C-II  
**Disposition:** the load-bearing proof chain is valid; the strongest merged explicit theorem `>0.598366` is certified; one minor optimizer presentation gap is repaired below; the hidden-edge proof itself supports a slightly stronger uniform coefficient and hence a certified `>0.5983685` floor  

## LEVEL I STATUS

`STILL OPEN`.

This audit does not inherit PR #182's self-classifications. It reads the 13 theorem reports and 4 exact certificate scripts as separate proof objects, reconstructs the actual dependency graph, checks the imported Bonnesen statement at theorem level, reruns every exact certificate independently, and separates endpoint statements from the later stronger explicit constants.

The principal conclusions are:

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge \lambda_{HE}>0.598366
}
\]

from the merged hidden-edge report, and the slightly stronger audit consequence

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
>0.5983685.
}
\]

The latter uses no new geometric hypothesis; it only spends the uniform margin already present in the two cases of the HE proof.

The numerical improvement is small and is superseded as a research lead by the much stronger PR #188 renormalized-surplus chain if that chain is promoted. Its value here is independent certification of the older RSR/DD branch.

---

## 1. Audited file set and dependency graph

PR #182 contains the following theorem progression.

```text
RSR inequality + FSDB + ZK/GU + JC + DD + DB
  -> RD two-obstruction feasible region
  -> RX exact optimizer and >0.598 floor
  -> SL endpoint ledger
  -> AC attachment-area concentration
  -> ND nested-disk endpoint exclusion

BV boundary-vertex isodiametric defect
  -> BRD constant-coefficient optimizer >0.5983
  -> BVE exact surplus-dependent defect function
  -> BF feedback optimizer >0.59834
  -> CW constant-width endpoint exclusion
  -> HE hidden-edge boundary-sharing defect
  -> HX constant-coefficient optimizer >0.598366

PC + DD + JC
  -> PD pocket-degree Dirichlet cavity theorem
     (valid theorem; its displayed ~0.767 optimizer is explicitly exploratory only)
```

The final HX theorem does **not** depend on the qualitative ND or CW endpoint exclusions. Conversely, CW's nonattainment gap concerns the exact BVE endpoint `lambda_BVE`, not the later HX endpoint `lambda_HE`. These claims must remain scoped separately.

---

## 2. Imported Bonnesen theorem

BV/BVE/HE use the following planar theorem.

For every compact convex planar body with area `A` and perimeter `P`, there exist concentric inscribed/circumscribed circles with radii `r_1<=r_2` such that

\[
\boxed{
(r_2-r_1)^2\le\frac{P^2-4\pi A}{4\pi}.
}
\]

This is the correct concentric-annulus Bonnesen theorem. It is stronger in form than the more familiar inequality written using the ordinary inradius and circumradius; the reports do not confuse the two versions.

The later arguments use only existence of one such concentric annulus, not uniqueness or equality classification.

---

## 3. RD/RX audit

Let

\[
\lambda=\lim\frac{e_{BB}+2s_C}{D},\qquad
y=\lim h/D,\qquad p=\lim P_F/D.
\]

The combined force-hull area lower bound is

\[
A(y,p)=\max\left\{\Phi(y),\Psi(p)\right\},
\]

with

\[
\Phi(y)=\frac{y+\sin y}{4},
\qquad
\Psi(p)=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2.
\]

RD correctly derives the two necessary inequalities

\[
A(y,p)-\frac\pi4\lambda^2
\le\frac{(\lambda+p-y)^2}{4\pi}
\tag{RD-JC}
\]

and

\[
A(y,p)-\frac\pi4\lambda^2
\le
\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
\tag{RD-DD}
\]

The nontrivial DD reduction introduces

\[
z=(Q+2s_Z)/D
\]

and upper-bounds the cavity by

\[
F_{y,p}(z)=
\frac1{\sqrt6}(2y-z)^{3/2}\sqrt{2y-z-p}
+\frac{z^2}{4\pi}.
\]

The derivative sign in RD is correct. On the feasible interval,

\[
F'_{y,p}(z)<0,
\]

so replacing `z` by zero is genuinely the worst relaxation rather than an unjustified endpoint guess.

RX's optimizer calculus was rederived. The area crossover

\[
p_e(y)=2+2\sqrt{\Phi(y)/c_R},
\qquad c_R=\pi/(\pi-2)^2,
\]

has `p_e'(y)<1/2`, hence `m(y)=p_e(y)-y` decreases. On the crossover, the DD threshold decreases and the JC threshold increases. The pre-transition JC/DD intersection has implicit equation

\[
F(y,\lambda)
=y+\lambda-2\sqrt{\pi S}-{3S^2\over4y^3}=0,
\qquad
S=\Phi(y)-{\pi\over4}\lambda^2,
\]

with `F_lambda>0` and the certified rational estimate

\[
F_y>{639\over19600}>0.
\]

Therefore the crossing threshold decreases before the unique transition.

For `y>=pi/2`, the global lower-bound argument does not need to know the DD crossover geometry: `max(J,D)>=J`, and the fixed-`y` JC minimum is the area-crossover value, which increases beyond the transition. This observation repairs a minor presentation overstatement in RX/HX where the text says the full fixed-`y` maximum itself equals the JC crossover throughout the entire right branch. The theorem only needs the lower bound and remains valid.

The exact RX certificate was independently rerun and passes.

---

## 4. Endpoint chain SL -> AC -> ND

### SL

At the exact RX endpoint, strictness of the `z` relaxation forces

\[
Q=o(D),\qquad s_Z=o(D).
\]

Because the DD endpoint has a positive normalized detour, equality in the relaxation

\[
x_B+a\le b
\]

forces

\[
q-a=o(D).
\]

PC then gives

\[
d_P=o(D),\qquad d_H=o(D),
\]

and the remaining component ledger yields the stated linear singleton lower bound. These implications are valid; none assumes a pocket-to-component injection.

### AC

Endpoint saturation of the attachment-cell area budget gives

\[
\sum_r\delta_r/D\to\lambda_{RD},
\qquad
\sum_r\delta_r^2/D^2\to\lambda_{RD}^2.
\]

The inequality

\[
\sum_r\delta_r^2\le(\max_r\delta_r)\sum_r\delta_r
\]

therefore forces one component with

\[
\delta_*/D\to\lambda_{RD}
\]

and total diameter `o(D)` in all other components. The dominant attachment polygon saturates planar isodiametry, so every normalized Hausdorff limit is a disk of diameter `lambda_RD`.

### ND

Every vertex of the dominant attachment polygon is a loaded force-hull boundary vertex. Polygon convergence to a disk forces maximum normalized edge length to zero, hence the polygon vertices become dense on the limiting circle.

The boundary-limit lemma used by ND is correct for convex Hausdorff convergence: if `x_j in partial C_j`, choose supporting normals `u_j`; after extracting `u_j->u`, uniform support-function convergence gives `x.u=h_C(u)`, hence `x in partial C`.

Thus the whole limiting disk boundary lies on the limiting force-hull boundary. A convex body cannot strictly contain a nondegenerate disk while preserving the disk's entire boundary. Since the force-hull limit has diameter one but the disk has diameter `lambda_RD<1`, the endpoint is impossible.

The diagonal-sequence argument then gives a nonexplicit positive gap above `lambda_RD`. ND is valid.

---

## 5. BV/BVE boundary-sharing audit

### BV

Let `K subset F`, `V(K) subset partial F`, `diam K=d<=3D/5`. Bonnesen gives a concentric annulus. With normalized half-width parameter `x=2(r_2-r_1)/d`, one obtains

\[
B(c,{d\over2}(1-x))\subset K\subset B(c,{d\over2}(1+x)).
\]

The adjacent polygon-edge support normals are each within an angle

\[
\alpha=\arccos{1-x\over1+x}
\]

of the corresponding vertex radial direction. Since the inner disk is nondegenerate, the cyclic radial directions of the vertices cover the circle; consecutive gaps are at most `2alpha`. Every support normal of `F` at a shared polygon vertex is also a support normal of `K` there and therefore lies in the polygon normal cone. This makes the selected force-hull support normals a `2alpha`-net.

The resulting radial support estimate

\[
D\le d\frac{(1+x)^3}{1-6x+x^2}
\]

is correct. The constant BV loss `1/1600` follows.

### BVE

The exact root `kappa(c)` of

\[
c(1+\kappa)^3=1-6\kappa+\kappa^2
\]

correctly packages the same support-normal argument and yields

\[
area(K)\le
\left({\pi\over4}-{\kappa(c)^2\over4}\right)d^2.
\]

The defining rational function is strictly increasing in `x` on the stated interval, so the direction of the contradiction is correct. Applying BVE cellwise with `c=lambda+eta` and then `eta downarrow0` correctly yields the surplus-dependent attachment coefficient `G(lambda)`.

---

## 6. BRD/BF/CW audit

BRD is the constant-BV-coefficient rerun of RX. Its monotonicity and exact `>0.5983` certificate are valid.

BF replaces the constant coefficient by BVE's increasing `G(lambda)`. The fixed-`y` threshold monotonicities remain correct; differentiating the JC root gives a positive right-branch derivative because

\[
\pi c_R(p-2)>\lambda+p-y.
\]

The pre-transition implicit derivative uses the same robust `F_y>639/19600` lower bound. The BVE exact certificate independently passes and proves `lambda_BVE>0.59834`.

CW's endpoint exclusion is also valid. Saturation concentrates component diameter into one attachment hull `K_D`. If `P_D/d_D` stayed below `pi` by a fixed amount, Bonnesen would force an annulus parameter strictly below `kappa(lambda_BVE)`, while the BVE support-normal inequality would then give

\[
1<1
\]

in the limit. Therefore `P_D/d_D->pi`.

A planar convex Hausdorff limit of diameter `lambda_BVE` and perimeter `pi lambda_BVE` has every directional width equal to `lambda_BVE`; it is a constant-width body. The supplied proof that a constant-width planar body has no boundary segment is correct. Polygon vertices therefore become dense on its boundary, and the same boundary-limit plus nested-convexity argument as ND forces the full force hull to equal the smaller body, contradicting diameter one.

Thus CW gives a nonexplicit gap above the **BVE endpoint** `lambda_BVE`. It does not assert a gap above the later hidden-edge endpoint.

---

## 7. HE hidden-edge theorem

HE's extra strictness is genuine.

Choose an exterior force-hull point `y` at distance at least `D/2` from the Bonnesen center. Because the attachment polygon lies in a strictly smaller outer annulus, `y` lies outside it. The two tangent rays from `y` bracket a visible polygon-boundary arc. That arc becomes strictly interior to `conv(K union {y})`, so it cannot contain a polygon vertex because every polygon vertex lies on `partial F`. Hence the visible arc is contained in one polygon edge.

The tangent geometry gives a uniform edge-length lower bound. The subsequent perimeter lemma is correct: if a diameter-`d` convex body contains a boundary segment of length `ell`, then in the segment-normal direction its width is at most

\[
\sqrt{d^2-\ell^2/4}.
\]

The width function is `d`-Lipschitz in angular distance because it is the support function of `K-K subset B(0,d)`. Integrating the resulting triangular width deficit gives

\[
\pi d-P
\ge d\left(1-\sqrt{1-\ell^2/(4d^2)}\right)^2.
\]

Feeding this perimeter deficit into Bonnesen yields HE.3.

No step uses RSR equality uniqueness.

---

## 8. Audit strengthening of HE

The published HE statement deliberately rounds its loss down to

\[
{3\over4000}=0.00075.
\]

Its own case split proves more.

If

\[
x\ge{11\over200},
\]

Bonnesen immediately gives

\[
{A\over d^2}
\le{\pi\over4}-{x^2\over4}
\le{\pi\over4}-{121\over160000}.
\tag{HE+1}
\]

If `x<11/200`, HE proves `x>51/1000` and one hidden edge of normalized length at least

\[
r={69363\over200000}.
\]

Put

\[
s_0={r^4\over64}.
\]

The same Bonnesen feedback gives the exact loss

\[
{1\over4}\left({51\over1000}\right)^2
+{s_0\over2}-{s_0^2\over12}.
\]

Exact rational arithmetic gives

\[
{1\over4}\left({51\over1000}\right)^2
+{s_0\over2}-{s_0^2\over12}
>{121\over160000}.
\tag{HE+2}
\]

Therefore the proof actually establishes:

### Theorem HE+

Under the hypotheses of HE,

\[
\boxed{
area(K)
\le
\left({\pi\over4}-{121\over160000}\right)\,diam(K)^2.
}
\tag{HE+3}
\]

The target-C cell corollary follows verbatim for `lambda<3/5`.

---

## 9. HE+ optimizer and exact certificate

Let

\[
c_+= {\pi\over4}-{121\over160000}.
\]

Replace `c_HE` by `c_+` in HX. The optimizer proof is unchanged: the fixed-`y` JC threshold decreases to the FSDB/RSR crossover and increases after it; the DD crossover value decreases, the JC crossover value increases, and the pre-transition crossing has `F_y>0` by the same rational estimates. For `y>=pi/2`, it is enough to use the increasing fixed-`y` JC lower bound as explained in Section 3 of this audit.

The companion certificate `research/verify_pr182_heplus_05983685.py` uses only exact `Fraction` arithmetic. At

\[
y_0={15245283\over10^7}=1.5245283
\]

it proves

\[
0.5115690768
<\sqrt{\Phi(y_0)/c_R}
<0.5115690769,
\]

\[
0.5983685<r_+(y_0)<0.5983686,
\]

and

\[
d_+(y_0)>0.598369.
\]

Thus `y_0` lies strictly before the unique crossover, and monotonicity gives

\[
\boxed{
\lambda_+>0.5983685.
}
\]

This is a theorem-level audit strengthening, not a floating-point extrapolation.

---

## 10. Pocket-degree Dirichlet theorem

`target_c_pocket_degree_dirichlet_cavity_2026-09-10.md` is mathematically valid and should not be lost merely because the PR later followed the boundary-sharing branch.

Writing an OP pocket chain length as

\[
\ell_P=2+r_P,
\qquad\sum r_P=d_P,
\]

the exact convexity/concentration identity gives

\[
\sum_P\ell_P^3
\le(d_P+2)^3+8(a-1).
\]

Combining with DD yields the finite PD.1 bound. After normalization, PC gives

\[
d+\xi\le\lambda,
\qquad
\xi=Q/D,
\]

and the exceptional-face allocation inequality

\[
{1\over\sqrt6}(1-a)^{3/2}\sqrt{r-a}+{a^2\over4\pi}
\le{1\over\sqrt6}\sqrt r
\]

is correct for `0<=a<=min(1,r)`. Hence

\[
\boxed{
A(y,p)-{\pi\over4}\lambda^2
\le{1\over\sqrt6}\lambda^{3/2}\sqrt{2y-p}
}
\tag{PD}
\]

is a valid post-ZF necessary inequality.

The report's numerical optimizer near `0.76719537` is explicitly labeled exploratory and has no rigorous global optimizer proof or certificate in PR #182. This audit therefore certifies PD itself, **not** the `0.767...` decimal as a theorem.

---

## 11. Certificate reruns

The four merged scripts were independently reproduced with exact rational arithmetic and all assertions passed:

- `verify_rsr_dd_0598.py`;
- `verify_bv_rsr_dd_05983.py`;
- `verify_bve_rsr_dd_059834.py`;
- `verify_hidden_edge_rsr_dd_0598366.py`.

Representative exact-sign decimal diagnostics after the rational assertions passed:

```text
RX:
  JC residual at 0.598      = -1.2324e-3
  JC residual at 0.599      = +1.3873e-2
  DD margin at 0.599        = +1.1155e-4

BV:
  JC residual at 0.5983     = -3.1932e-4
  JC residual at 0.59832    = +4.8423e-7
  DD margin at 0.5986       = +7.9092e-5

BVE:
  JC residual at 0.59834    = -2.4864e-7
  JC residual at 0.598341   = +1.0255e-6
  DD margin at 0.598341     = +6.9826e-7

HE:
  JC residual at 0.598366   = -8.4752e-7
  JC residual at 0.598367   = +4.2517e-7
  DD margin at 0.598367     = +3.6341e-6
```

The new HE+ certificate is stored separately and has positive outward-rounded margins.

---

## 12. Final classification

| Object | Independent audit disposition |
| --- | --- |
| RD two-obstruction system | valid |
| RX optimizer and `>0.598` | valid |
| SL endpoint ledgers | valid |
| AC concentration | valid |
| ND endpoint exclusion / nonexplicit gap | valid |
| BV boundary-vertex defect | valid |
| BRD `>0.5983` | valid, superseded |
| BVE exact defect function | valid |
| BF `>0.59834` | valid, superseded |
| CW BVE-endpoint exclusion | valid, scoped to `lambda_BVE` |
| HE hidden-edge theorem | valid |
| HX `lambda_HE>0.598366` | **certified valid** |
| qualitative gap above `lambda_HE` | not claimed/proved by PR #182 |
| HE+ coefficient `pi/4-121/160000` | **proved by existing HE case split** |
| HE+ scalar floor `>0.5983685` | **proved by audit + exact certificate** |
| PD cavity theorem | valid |
| PD numerical `~0.76719537` optimizer | exploratory, not certified |
| RSR disk-equality uniqueness | not used; unavailable from cited source |
| Level I | still open |

PR #182 should no longer be labeled merely `audited-working`. Its explicit RSR/DD/boundary-sharing theorem stack has now received a full independent audit. The strongest certified consequence from this stack is the HE+ floor above `0.5983685`, while PD remains a promising stronger unoptimized theorem.
