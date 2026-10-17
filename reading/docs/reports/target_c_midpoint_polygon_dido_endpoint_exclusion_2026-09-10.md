> Generated reading edition · [exact source](../../../docs/reports/target_c_midpoint_polygon_dido_endpoint_exclusion_2026-09-10.md) · source SHA-256 `d83192c6cb3295f873e1b5ede6a2442ba6c90b3fe8341d8c053e446ac975be54`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8EE34F5C8FBC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_midpoint_polygon_dido_endpoint_exclusion_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=fb0f1bcb21b244b74c8663291a245173f433212b; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FS midpoint-polygon rigidity excludes the Dido pocket endpoint

**Date:** 2026-09-10  
**Repository state:** branch `research/c99-c2-dpc-20260910-sol` after the Dido pocket commit; contemporaneous `main` head `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Run type:** closing proof / endpoint rigidity / adversarial audit  
**Target:** Target C, C-II after ZF/DB/FSDB/DIDO  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** no theorem imported  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`

The preceding Dido report proves

$$
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DIDO}
=0.8316870417755330\ldots .
$$

and identifies the equality endpoint: `h/D -> y_*`, `d_P/D -> lambda_DIDO`, all normalized `Q,s_C,d_H,s_Z,c_B` vanish, and one outer pocket carries asymptotically all macroscopic chain length.

This report proves that the equality endpoint is impossible. The decisive new finite theorem is stronger than the one-sided inclusion used in FSDB:

$$
\boxed{
 d_{\rm Haus}\left(F-o,\frac12P_H\right)\le L_D=o(D).
}
\tag{MP.1}
$$

Here `P_H=D conv{+-u_e}` is the full actual diameter-direction polygon and `o,L_D` are the common source circumcenter and midpoint error from FS.4.

At the Dido endpoint, equality in the FSDB area floor then forces the diameter-direction gaps into their exact concavity equality pattern: one macroscopic projective gap and all remaining excess gap mass vanishing. Because projective gaps repeat antipodally, `P_H/2` has two opposite macroscopic sides. MP.1 and the FS radial annulus force those limiting sides to be actual macroscopic force-hull sides, hence two distinct OP pockets. Their combined pocket-degree mass exceeds `D`, while the Dido endpoint requires total `d_P< D`. Contradiction.

Therefore there exist absolute constants `epsilon_MP>0` and `D_0<infinity` such that every sufficiently large post-ZF survivor satisfies

$$
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DIDO}+\epsilon_{MP}.
}
\tag{MP.2}
$$

The gap is nonexplicit. Level I remains open above it.

## 1. Starting endpoint

Use the exact notation of

- `target_c_full_source_circumradius_response_2026-09-10.md` (FS),
- `target_c_post_zf_difference_body_perimeter_2026-09-09.md` (DB),
- `target_c_fs_symmetric_difference_body_area_2026-09-10.md` (FSDB), and
- `target_c_dido_pocket_surplus_08316_2026-09-10.md` (DIDO).

For every actual diameter edge `e=bk`, choose one orientation

$$
p_b-p_k=D u_e,
\qquad |u_e|=1,
$$

and define

$$
P_H:=D\,conv\{\pm u_e:e\in E(H)\}.
\tag{1.1}
$$

FS.4 gives a common full-source circumcenter `o` and

$$
L_D=O(D^{3/4})=o(D)
$$

such that every actual diameter midpoint satisfies

$$
\left|\frac{p_b+p_k}{2}-o\right|<L_D.
\tag{1.2}
$$

It also gives the radial annulus, uniformly for every actual diameter endpoint `b`:

$$
\boxed{
\frac D2-\eta<|p_b-o|<\frac D2+\eta,
\qquad
\eta=3^{1/4}\sqrt D=o(D).
}
\tag{1.3}
$$

The implication attacked is

```text
FS midpoint localization
    -> force hull is two-sided o(D)-close to half the full diameter-direction polygon
    + Dido endpoint forces equality in the FSDB area inequality
    -> diameter-direction concavity equality
    -> two opposite macroscopic flat sides of P_H/2
    + radial annulus
    -> two actual macroscopic missing sides of F
    -> two macroscopic OP pockets
    -> d_P/D>1
    -> contradiction with d_P/D -> lambda_DIDO<1.
```

## 2. Strongest new finite theorem: two-sided midpoint polygon

### Theorem MP — midpoint-polygon Hausdorff theorem

For every C-II source to which FS.4 applies,

$$
\boxed{
 d_{\rm Haus}\left(F-o,\frac12P_H\right)\le L_D.
}
\tag{MP.3}
$$

This is an exact finite statement.

#### Proof

Fix an actual diameter edge `e=bk` and orient it so

$$
p_b-p_k=D u_e.
$$

Let

$$
m_e:=\frac{p_b+p_k}{2}.
$$

Then

$$
p_b-o=\frac D2u_e+(m_e-o),
\qquad
p_k-o=-\frac D2u_e+(m_e-o).
\tag{2.1}
$$

By FS.4, `|m_e-o|<L_D`. Hence both generator points

$$
\pm\frac D2u_e
$$

lie within `L_D` of actual points of `F-o`. Taking convex hulls over all diameter edges gives

$$
\frac12P_H\subseteq (F-o)+L_DB_2.
\tag{2.2}
$$

Conversely, every vertex used to form the force hull is an actual positive diameter endpoint, because the relative-interior stress has the full actual diameter support in the lexicographic C-II source. Thus for every such endpoint `b` there is an actual diameter edge `bk`. Equation (2.1) gives

$$
p_b-o\in\frac12P_H+L_DB_2.
$$

Taking the convex hull of all force-hull vertices gives

$$
F-o\subseteq\frac12P_H+L_DB_2.
\tag{2.3}
$$

Together (2.2)-(2.3) are MP.3. `square`

### Corollary MP.1 — asymptotic equality of area and perimeter

Along every unbounded C-II sequence,

$$
\boxed{
\operatorname{area}(F)
=
\frac14\operatorname{area}(P_H)+o(D^2),
}
\tag{2.4}
$$

and

$$
\boxed{
\operatorname{per}(F)
=
\frac12\operatorname{per}(P_H)+o(D).
}
\tag{2.5}
$$

#### Proof

For convex bodies at Hausdorff distance at most `L_D`, each lies in the `L_D` outer parallel body of the other. Steiner's formula and the diameter-perimeter bound `per<=pi diam`, together with `L_D=o(D)`, give an `o(D^2)` area difference and `o(D)` perimeter difference. Apply this to `F-o` and `P_H/2`. `square`

This strengthens FSDB's one-sided use of `(1/2)P_H subset F-o+L_DB_2`. It identifies the normalized force hull itself with the complete diameter-direction polygon asymptotically.

## 3. Dido endpoint forces equality in the FSDB area bound

Assume for contradiction that an unbounded survivor sequence satisfies

$$
\frac{e_{BB}+2s_C}{D}\to\lambda_{DIDO}.
\tag{3.1}
$$

DIDO gives

$$
\frac hD\to y_*,
\tag{3.2}
$$

where `y_*` is the unique Dido minimizer. It also gives

$$
\frac QD,\frac{s_C}D,\frac{d_H}D,\frac{s_Z}D,\frac{c_B}D\to0,
\qquad
\frac{d_P}D\to\lambda_{DIDO}.
\tag{3.3}
$$

Let `C_att` be the total attachment-cell area appearing in GU, so

$$
G=\operatorname{area}(F)-C_{att}.
\tag{3.4}
$$

DIDO gives the endpoint cavity upper bound

$$
\limsup\frac G{D^2}
\le
\lambda_{DIDO}^2
\widehat f\left(\frac{g(y_*)}{\lambda_{DIDO}}\right).
\tag{3.5}
$$

GU gives

$$
\limsup\frac{C_{att}}{D^2}
\le
\frac\pi4\lambda_{DIDO}^2.
\tag{3.6}
$$

By the defining Dido endpoint equality,

$$
\Phi(y_*)
=
\lambda_{DIDO}^2
\left[
\frac\pi4+
\widehat f\left(\frac{g(y_*)}{\lambda_{DIDO}}\right)
\right].
\tag{3.7}
$$

Thus (3.4)-(3.7) give

$$
\limsup\frac{\operatorname{area}(F)}{D^2}
\le\Phi(y_*).
\tag{3.8}
$$

FSDB gives the opposite inequality

$$
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge\Phi(y_*).
\tag{3.9}
$$

Therefore

$$
\boxed{
\frac{\operatorname{area}(F)}{D^2}
\to\Phi(y_*).
}
\tag{3.10}
$$

By MP.1,

$$
\frac{\operatorname{area}(P_H)}{D^2}
\to4\Phi(y_*)=y_*+\sin y_*.
\tag{3.11}
$$

## 4. Stability of the projective-gap concavity minimum

Let

$$
\delta_D=2\arcsin\frac1{2D}.
$$

Order the `h` projective diameter directions and write their gaps

$$
\gamma_1,\ldots,\gamma_h,
\qquad
\gamma_i\ge\delta_D,
\qquad
\sum_i\gamma_i=\pi.
\tag{4.1}
$$

DB/FSDB gives

$$
\frac{\operatorname{area}(P_H)}{D^2}
=\sum_i\sin\gamma_i.
\tag{4.2}
$$

Put

$$
B_D:=\pi-(h-1)\delta_D.
\tag{4.3}
$$

The exact concavity minimum is

$$
M_D:=(h-1)\sin\delta_D+\sin B_D.
\tag{4.4}
$$

Because `h/D->y_*` and `D delta_D->1`,

$$
B_D\to B_*:=\pi-y_*>0,
\qquad
M_D\to y_*+\sin y_*.
\tag{4.5}
$$

Equations (3.11), (4.2), and (4.5) imply

$$
\sum_i\sin\gamma_i-M_D\to0.
\tag{4.6}
$$

### Lemma MP.2 — one-gap stability

After cyclic relabeling,

$$
\boxed{
\gamma_1\to B_*=\pi-y_*;
}
\tag{4.7}
$$

and

$$
\boxed{
\sum_{i=2}^h(\gamma_i-\delta_D)\to0.
}
\tag{4.8}
$$

#### Proof

Write

$$
e_i:=\gamma_i-\delta_D\ge0.
$$

First, the second-largest `e_i` tends to zero. If two excesses `x,y` were both at least some fixed `epsilon>0` along a subsequence, merging them into one gap while resetting the other to `delta_D` would preserve the gap sum and decrease the sine sum by exactly

$$
\begin{aligned}
&\sin(\delta_D+x)+\sin(\delta_D+y)
-\sin\delta_D-\sin(\delta_D+x+y)\\
&\qquad=
4\sin\frac x2\sin\frac y2
\sin\left(\delta_D+\frac{x+y}{2}\right)>0.
\end{aligned}
\tag{4.9}
$$

The decrease has a positive lower bound depending only on `epsilon`, because here the total excess tends to `pi-y_*<pi`. The merged gap remains feasible. This contradicts (4.6) and the fact that `M_D` is the global minimum. Hence every excess except the largest is `o(1)` uniformly.

Let

$$
r_D:=\sum_{i=2}^h e_i
$$

after labeling `e_1=max e_i`. Pass to a subsequence on which `r_D->r>=0`. Because the maximum of the remaining gaps tends to zero,

$$
\sum_{i=2}^h(\gamma_i-\sin\gamma_i)\to0;
\tag{4.10}
$$

indeed `0<=x-sin x<=x^3/6` and the sum of all gaps is `pi`.

Since the total excess is `pi-h delta_D`,

$$
\gamma_1
=B_D-r_D.
\tag{4.11}
$$

Therefore

$$
\sum_i\sin\gamma_i-M_D
\to
r+\sin(B_*-r)-\sin B_*.
\tag{4.12}
$$

The right side vanishes only at `r=0`: its derivative with respect to `r` is

$$
1-\cos(B_*-r)\ge0,
$$

and it is strictly positive after integration over every interval of positive length. Equation (4.6) therefore forces `r=0`. This proves (4.8), and (4.11) gives (4.7). `square`

Thus the projective direction set has one macroscopic empty gap of angular size `B_*`; on the ordinary Euclidean circle of generators `+-D u_e/2`, that gap occurs twice, at antipodal positions.

## 5. A macroscopic side of the midpoint polygon transfers to an actual force-hull side

We need one elementary stability lemma.

### Lemma MP.3 — radial flat-side transfer

Let `Q_D` be a convex polygon with vertices on the radius-`D/2` circle centered at the origin. Let `F_D` be a convex polygon such that

1. `d_H(F_D,Q_D)=o(D)`;
2. every vertex of `F_D` has radius `D/2+o(D)` uniformly;
3. `Q_D` has a side whose endpoint directions have angular separation `B_D->B in (0,pi)`.

Then `F_D` has a side of length

$$
D\sin(B/2)+o(D).
\tag{5.1}
$$

#### Proof

Rotate so the side endpoints of `Q_D` have polar angles `+-B_D/2`. Its outward unit normal is the positive `x` direction, and its supporting line is

$$
x=\frac D2\cos(B_D/2).
\tag{5.2}
$$

Hausdorff closeness gives

$$
h_{F_D}(1,0)
\le
\frac D2\cos(B_D/2)+o(D).
\tag{5.3}
$$

Let `v` be any vertex of `F_D` whose polar angle `phi` lies between the two endpoint directions. Its radius is `D/2+o(D)`, so (5.3) gives

$$
\left(\frac D2+o(D)\right)\cos\phi
\le
\frac D2\cos(B_D/2)+o(D).
$$

Since `|phi|<=B_D/2` and `B` is bounded away from zero, this forces

$$
|\phi|\ge B_D/2-o(1).
\tag{5.4}
$$

Thus no force-hull vertex lies a fixed angular distance inside the open side sector; every such vertex is asymptotically in one of the two endpoint clusters.

There is at least one `F_D` vertex in each endpoint cluster. For an endpoint direction `u`, Hausdorff closeness gives

$$
h_{F_D}(u)\ge D/2-o(D).
$$

A maximizing vertex has radius at most `D/2+o(D)`, so its angular distance from `u` is `o(1)`.

For large `D`, `Q_D` contains a centered disk of radius `cD` for some fixed `c>0`, because its largest angular gap is bounded below `pi`; Hausdorff closeness then gives positive support in every direction for `F_D`, so the origin lies in the interior of `F_D`. Hence the cyclic order of vertices agrees with their polar-angle order. By (5.4), the last vertex in one endpoint cluster and the first vertex in the other are consecutive hull vertices. Their angular separation is `B_D-o(1)` and both radii are `D/2+o(D)`. Their distance is therefore

$$
2\frac D2\sin(B_D/2)+o(D)
=D\sin(B/2)+o(D).
$$

This consecutive pair is the required side. `square`

Apply MP.3 with

$$
Q_D=\frac12P_H,
\qquad
F_D=F-o.
$$

MP.3 supplies hypothesis 1, FS radial localization (1.3) supplies hypothesis 2, and MP.2 supplies two antipodal sides with

$$
B_D\to B_*=\pi-y_*.
$$

Therefore `F` has two distinct opposite-side sectors containing actual hull sides of lengths

$$
\boxed{
\left(\cos(y_*/2)+o(1)\right)D
}
\tag{5.5}
$$

each.

## 6. Two macroscopic missing sides contradict the Dido endpoint

The Dido endpoint lies in the active Dido range, so

$$
\frac{g(y_*)}{\lambda_{DIDO}}<z_0<1,
\qquad
\lambda_{DIDO}<1.
$$

Consequently

$$
g(y_*)<1.
\tag{6.1}
$$

Since `g` is strictly increasing and

$$
g(2\pi/3)=\frac{2\pi}{3}-1>1
$$

(using only `pi>3`),

$$
\boxed{y_*<2\pi/3.}
\tag{6.2}
$$

Thus

$$
\boxed{2\cos(y_*/2)>1>\lambda_{DIDO}.}
\tag{6.3}
$$

The two sides in (5.5) have length linear in `D`, hence exceed one for all sufficiently large `D`. They are therefore not unit-contact sides. Each is a missing force-hull side and, by OP, corresponds to a distinct outer pocket.

If the two pocket contact-chain lengths are `ell_1,ell_2`, the triangle inequality gives

$$
\ell_j\ge s_j.
$$

Since the pocket degree excess is `x_j=ell_j-2`, the total outer-pocket degree excess obeys

$$
\begin{aligned}
d_P
&\ge x_1+x_2\\
&\ge s_1+s_2-4\\
&=
\left(2\cos(y_*/2)+o(1)\right)D.
\end{aligned}
\tag{6.4}
$$

Hence

$$
\liminf\frac{d_P}{D}
\ge2\cos(y_*/2)>1.
\tag{6.5}
$$

But DIDO endpoint stability gave

$$
\frac{d_P}{D}\to\lambda_{DIDO}<1.
\tag{6.6}
$$

Equations (6.5)-(6.6) contradict each other. Therefore:

### Theorem MPE — Dido endpoint exclusion

There is no unbounded post-ZF C-II survivor sequence satisfying

$$
\frac{e_{BB}+2s_C}{D}\to\lambda_{DIDO}.
\tag{6.7}
$$

## 7. Uniform nonexplicit gap

### Corollary MPE.1

There exist absolute constants `epsilon_MP>0` and `D_0<infinity` such that every post-ZF C-II survivor with `D>=D_0` satisfies

$$
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DIDO}+\epsilon_{MP}.
}
\tag{7.1}
$$

#### Proof

If no such constants existed, choose for every integer `j` a survivor with `D_j>=j` and

$$
\frac{e_{BB}+2s_C}{D_j}
<\lambda_{DIDO}+\frac1j.
$$

DIDO.1 says every unbounded survivor sequence has liminf at least `lambda_DIDO`. Thus the chosen ratios converge to `lambda_DIDO`, contradicting MPE. `square`

No explicit value of `epsilon_MP` is claimed.

## 8. Exact target implication

The current report-level C-II state is now strictly stronger than a scalar lower bound:

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
>\lambda_{DIDO}
=0.8316870417755330\ldots
}
$$

in the uniform sense of (7.1).

The new finite theorem MP.3 also changes the structural interpretation of FS.4: the actual force hull is asymptotically the half diameter-direction polygon, so diameter-direction gap stability is directly force-hull side stability.

The shortest remaining Level I implication is still an upper/global incompatibility for the high-surplus regime. A sufficient next theorem is any universal post-ZF bound

$$
\limsup\frac{e_{BB}+2s_C}{D}
\le\lambda_{DIDO}
$$

(or any smaller constant), which would now immediately contradict MPE.1. Alternatively, a quantitative version of the two-flat-side argument may push the explicit lower bound upward enough to meet an existing planar upper ledger.

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| MP.3 Hausdorff midpoint-polygon theorem | proved finite | direct FS.4 midpoint identities in both directions |
| area/perimeter asymptotic equality | proved | convex parallel-body bounds |
| endpoint force-hull area saturation | proved | DIDO cavity upper + GU cell upper + FSDB lower |
| one-projective-gap stability | proved | exact sine merge identity + small-gap remainder |
| radial flat-side transfer | proved | support-function bound + FS annulus |
| two opposite macroscopic force-hull sides | proved at Dido endpoint | projective gap repeats antipodally |
| Dido endpoint exclusion | proved under DIDO dependencies | two-side pocket mass exceeds total endpoint `d_P` |
| uniform positive gap above `lambda_DIDO` | proved nonexplicitly | sequential compactness contradiction |
| Level I | still open | no global upper bound on the high-surplus currency yet |

## 10. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its direction gaps are all microscopic; MP simply identifies its near-disk force hull with the corresponding direction polygon, and it does not satisfy the Dido endpoint equality geometry |
| dense isolated fillings | yes | MP concerns the actual force hull, while FS.4's common center is obtained from the entire source including isolates; no small-isolate assumption is added |
| one giant outer pocket | yes | MPE does not forbid one giant pocket in general; it proves that Dido endpoint area equality simultaneously forces two opposite macroscopic force-hull sides |
| finite subdivision of an opposite limiting flat | passed | FS radial annulus forbids vertices a fixed distance into the flat-side sector, so the subdivision collapses to endpoint clusters and an actual long edge remains |
| response trace shell | yes | no response-operator norm or trace inference is used |

The decisive global-optimality input remains the full-source FS/FSDB/GU chain. The midpoint theorem itself is geometric; the endpoint contradiction becomes source-specific only because equality in the whole-source gap forces FSDB area saturation.

## 11. Failed routes and no-go results

1. Hausdorff central symmetry alone is insufficient to duplicate a finite pocket. MP avoids this by identifying `F` with the complete diameter-direction polygon and then using the radial annulus.
2. A qualitative Hopf-Pannwitz diameter-graph classification is unnecessary for this endpoint. The projective gap concavity ledger already gives the required two opposite flat sides.
3. No conductance or positive-minor magnitude floor is used; those remain unavailable.

## 12. Canonical promotion recommendation

**Hold as report pending independent audit.** MP.3 is a clean finite consequence of FS.4 and is a strong promotion candidate. MPE depends on the unpromoted DIDO/FSDB/DB/PC chain and should be promoted only after that chain is independently checked.

If promoted, update the Target C route map and active continuation prompt to record the explicit `lambda_DIDO` floor plus the nonexplicit uniform gap above it.

## 13. Next run

Quantify the flat-side argument away from exact Dido equality. The current contradiction has a large endpoint margin:

$$
2\cos(y_*/2)>1>\lambda_{DIDO}.
$$

A stability inequality converting an FSDB area excess above its concavity minimum into a lower bound on the second macroscopic gap, and then into `d_P`, should turn the nonexplicit endpoint exclusion into a larger explicit surplus floor. This is the highest-value continuation before attempting a new route.

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New finite theorem:
For P_H=D conv{+-u_e} and the FS.4 common center o,
    d_Haus(F-o,P_H/2)<=L_D=O(D^(3/4))=o(D).
Every loaded endpoint also has radius D/2+o(D).

Dido endpoint lambda_DIDO=0.8316870417755330... forces
    h/D -> y_*,
    area(F)/D^2 -> Phi(y_*),
    d_P/D -> lambda_DIDO,
    Q,s_C,d_H,s_Z,c_B=o(D).
Midpoint-polygon equality then forces the projective direction gaps to have exactly
one macroscopic gap B_*=pi-y_*; it appears twice antipodally in P_H/2.
The radial annulus transfers these to two actual F sides of length
    (cos(y_*/2)+o(1))D.
Both are missing contact sides, hence their two OP pockets give
    liminf d_P/D >= 2cos(y_*/2).
Since the Dido endpoint is active and lambda_DIDO<1,
    g(y_*)<1<g(2pi/3),
so y_*<2pi/3 and 2cos(y_*/2)>1>lambda_DIDO.
Contradiction.

Therefore there are epsilon_MP>0,D0 such that every post-ZF survivor with D>=D0 has
    (e_BB+2s_C)/D >= lambda_DIDO+epsilon_MP.

Next:
quantify gap/flat-side stability away from exact equality to make epsilon_MP explicit
and push toward a high-surplus contradiction.
```
