> Generated reading edition · [exact source](../../../docs/reports/target_c_external_annulus_saturation_2026-09-10.md) · source SHA-256 `80e891f3731687ab147f127c84bfe6f18fcc059e400db38b1371bc902acfbb39`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AD79EA7DC1B7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — external annulus saturation in the low-surplus branch

**Date:** 2026-09-10  
**Repository state:** PR #178 after MP commit `7e7505aa8686952b1bb2d37a6120eba959551e10`  
**Run type:** closing-proof continuation / source-population transfer  
**Target:** Target C, C-II  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md` with the promoted September 9 C-I correction  
**External web search:** used to recheck the stated Mazel--Stuhl--Suhov Voronoi-cell constant behind AV  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

MP proves that every fixed pinned/contact-surplus regime below

$$
\lambda_{\rm disk}=0.693272542288314\ldots
$$

has a uniform linear force-hull perimeter deficit.  This report pushes that geometric
loss through the full-source population rather than stopping at perimeter.

The result is a new normal form for the low-surplus branch:

1. a positive fraction of the source area lies in the annulus between the force hull
   `F` and the full source hull `K`;
2. a positive fraction of the source points are contact-isolated points in that
   annulus; and
3. those external isolated points asymptotically saturate the triangular packing
   density in the annulus, with only `O(D)` population error.

Thus the remaining low-surplus obstruction is not an arbitrary collection of
isolates.  Global optimality forces a dense near-contact external sea around the
force-visible core.

---

## 1. Starting endpoint and implication chain

Let

$$
Z_{ext}:=|A\setminus F|
$$

for the contact-isolated source points outside the force hull, and put

$$
A_{ann}:=\operatorname{area}K-\operatorname{area}F.
$$

The new chain is

```text
MP: low pinned/contact surplus
    -> per(F) <= (pi-epsilon)D
isoperimetry
    -> area(F) <= (pi/4-eta)D^2
full-source Oler + global lattice comparison
    -> area(K) = pi D^2/4-O(D)
    -> A_ann >= eta D^2-O(D)
ER lower population + AV upper annular capacity
    -> Z_ext = (2/sqrt(3)) A_ann + O(D)
    -> Z_ext = Theta(D^2)
```

A scaled version of AV then shows that the minimum pair separation inside the external
population is `1+O(1/D)`.  This last statement does **not** create an exact unit
contact and is not used as a false compactness shortcut.

---

## 2. Dependency audit

### 2.1 Whole-source area deficit is only linear

For the full source hull `K`, the exact whole-source notation is

$$
\delta_K=\frac\pi4D^2-\operatorname{area}K,
$$

$$
\mathscr O_A
=\operatorname{area}K+rac{\sqrt3}{4}\operatorname{per}K
-\frac{\sqrt3}{2}(n-1).
$$

Oler gives `mathscr O_A>=0`, while the strict translated-lattice comparison at the
actual global optimum gives

$$
\delta_K+\mathscr O_A
<\frac{\sqrt3}{4}\operatorname{per}K.
$$

Therefore

$$
\boxed{
0\le\delta_K
<\frac{\sqrt3}{4}\operatorname{per}K
\le\frac{\sqrt3\pi}{4}D.
}
\tag{AS.1}
$$

In particular

$$
\boxed{
\operatorname{area}K
=\frac\pi4D^2-O(D).
}
\tag{AS.2}
$$

This is a full-source global-optimality statement; it is not inferred from force-hull
geometry.

### 2.2 ER lower bound

The report `target_c_external_rattler_force_area_dichotomy_2026-09-09.md` proves

$$
\boxed{
Z_{ext}
>
\frac2{\sqrt3}
\left(\frac\pi4D^2-\operatorname{area}F\right)
-\frac12\operatorname{per}F.
}
\tag{AS.3}
$$

Since

$$
\frac\pi4D^2-\operatorname{area}F
=A_{ann}+\delta_K,
$$

and `delta_K>=0`, ER immediately yields the weaker but annulus-aligned lower bound

$$
\boxed{
Z_{ext}>
\frac2{\sqrt3}A_{ann}-\frac12\operatorname{per}F.
}
\tag{AS.4}
$$

### 2.3 AV upper bound

The September 10 report
`target_c_annular_voronoi_matching_exclusion_2026-09-10.md` proves for any
unit-separated set in `K\setminus int(F)`

$$
\boxed{
|S|\le
\frac2{\sqrt3}
\left(
\operatorname{area}K-\operatorname{area}F
+\operatorname{per}K+\operatorname{per}F+\pi
\right).
}
\tag{AS.5}
$$

Applying this to the external isolated source points gives

$$
\boxed{
Z_{ext}\le
\frac2{\sqrt3}
\left(
A_{ann}+\operatorname{per}K+\operatorname{per}F+\pi
\right).
}
\tag{AS.6}
$$

AV's only non-elementary input is the planar local Voronoi-cell bound: in a packing of
unit disks, a bounded Voronoi cell has area at least `2sqrt(3)`.  The cited
Mazel--Stuhl--Suhov paper states that exact minimum and equality at the perfect
hexagon.  Scaling lengths by `1/2` gives `sqrt(3)/2` for center separation one.  AV's
maximal extension proves all cells used in its argument are bounded, so the imported
hypothesis matches.

---

## 3. Theorem AS — annular density saturation

### Theorem AS.1 — exact two-sided annular population squeeze

Every post-ZF C-II survivor satisfies

$$
\boxed{
\frac2{\sqrt3}A_{ann}-\frac12\operatorname{per}F
< Z_{ext}
\le
\frac2{\sqrt3}
\left(A_{ann}+\operatorname{per}K+\operatorname{per}F+\pi\right).
}
\tag{AS.7}
$$

Consequently, uniformly over every unbounded survivor sequence,

$$
\boxed{
Z_{ext}
=\frac2{\sqrt3}A_{ann}+O(D).
}
\tag{AS.8}
$$

### Proof

The lower half is AS.4 and the upper half is AS.6.  Cauchy's
perimeter--diameter inequality gives

$$
\operatorname{per}F,\operatorname{per}K\le\pi D,
$$

so the two error terms in AS.7 are `O(D)`. `square`

### Scope

AS.7 is source-specific.  Its upper half is a general annular packing theorem, but its
lower half uses the strict global translated-lattice comparison at `D(n)` through ER.
It therefore does not apply to a merely dense triangle-free shell filling with no
global-optimality certificate.

---

## 4. Low-surplus branch forces a quadratic saturated annulus

### Theorem AS.2

Fix

$$
\lambda_0<\lambda_{\rm disk}.
$$

Then there exist constants

$$
\eta(\lambda_0)>0,
\qquad
c(\lambda_0)>0,
\qquad
D_0(\lambda_0)<\infty
$$

such that every post-ZF survivor with `D>=D_0` and

$$
\frac{e_{BB}+2s_C}{D}\le\lambda_0
\tag{AS.9}
$$

satisfies

$$
\boxed{A_{ann}\ge\eta(\lambda_0)D^2,}
\tag{AS.10}
$$

$$
\boxed{Z_{ext}\ge c(\lambda_0)D^2,}
\tag{AS.11}
$$

and

$$
\boxed{
\frac{Z_{ext}}{A_{ann}}
\longrightarrow\frac2{\sqrt3}
}
\tag{AS.12}
$$

uniformly along any unbounded sequence satisfying AS.9.

### Proof

By MP.2 there is `epsilon=epsilon(lambda_0)>0` such that for all sufficiently large
such survivors

$$
\operatorname{per}F\le(\pi-\epsilon)D.
\tag{AS.13}
$$

The planar isoperimetric inequality gives

$$
\operatorname{area}F
\le\frac{\operatorname{per}(F)^2}{4\pi}
\le
\frac{(\pi-\epsilon)^2}{4\pi}D^2.
\tag{AS.14}
$$

Define

$$
\eta_0
:=\frac\pi4-
\frac{(\pi-\epsilon)^2}{4\pi}
=\frac{2\pi\epsilon-\epsilon^2}{4\pi}>0.
\tag{AS.15}
$$

AS.2 gives

$$
\operatorname{area}K
=\frac\pi4D^2-O(D).
$$

Subtract AS.14:

$$
A_{ann}\ge\eta_0D^2-O(D).
$$

After increasing `D_0`, AS.10 holds with, for example,

$$
\eta(\lambda_0)=\eta_0/2.
$$

Insert AS.10 into the lower half of AS.7.  Since `per(F)=O(D)`, for large `D`

$$
Z_{ext}\ge\frac{\eta(\lambda_0)}{\sqrt3}D^2,
$$

after another harmless increase in `D_0`; this proves AS.11.

Finally AS.7 says

$$
Z_{ext}=\frac2{\sqrt3}A_{ann}+O(D),
$$

while AS.10 gives `A_ann=Omega(D^2)`.  Divide by `A_ann` to obtain AS.12. `square`

This eliminates the possibility that MP's perimeter-deficient low-surplus branch is
paid only by a thin boundary layer.  It must contain a macroscopic annulus and a
quadratic external population.

---

## 5. The external isolated set is microscopically near contact

Let

$$
s_{ext}:=\min\{|x-y|:x,y\in A\setminus F,\ x\ne y\}.
$$

In the AS.2 regime `Z_ext=Theta(D^2)`, so this is defined for large `D`.  Because the
points are contact-isolated,

$$
s_{ext}>1.
$$

### Theorem AS.3

Under the hypotheses of AS.2,

$$
\boxed{s_{ext}=1+O_{\lambda_0}(D^{-1}).}
\tag{AS.16}
$$

### Proof

Set `s=s_ext` and scale `K,F` and the external point set by `1/s`.  The scaled external
points are unit-separated, so AV gives

$$
Z_{ext}\le\frac2{\sqrt3}
\left(
\frac{A_{ann}}{s^2}
+\frac{\operatorname{per}K+\operatorname{per}F}{s}
+\pi
\right).
\tag{AS.17}
$$

AS.4 gives simultaneously

$$
Z_{ext}>
\frac2{\sqrt3}A_{ann}-\frac12\operatorname{per}F.
\tag{AS.18}
$$

Compare the two and multiply by `sqrt(3)/2`:

$$
A_{ann}\left(1-\frac1{s^2}\right)
<
\frac{\sqrt3}{4}\operatorname{per}F
+\frac{\operatorname{per}K+\operatorname{per}F}{s}
+\pi.
\tag{AS.19}
$$

Since `s>=1`, both perimeters are at most `pi D`, and AS.10 gives
`A_ann>=eta D^2`,

$$
0\le1-\frac1{s^2}
\le\frac{C(\lambda_0)}D
\tag{AS.20}
$$

for a fixed constant `C(lambda_0)`.  For large `D` the right side is below `1/2`, so

$$
s\le\left(1-\frac{C(\lambda_0)}D\right)^{-1/2}
=1+O_{\lambda_0}(D^{-1}).
$$

Together with `s>1`, this proves AS.16. `square`

AS.3 is deliberately only a near-contact statement.  It does not promote these pairs
to unit contacts, does not put them into the KKT support, and does not identify them
with the nonisolated core.

---

## 6. Exact effect on the C-II endpoint

For every fixed `lambda_0<lambda_disk`, a sufficiently large survivor satisfying
AS.9 is now forced into all of the following simultaneously:

$$
\pi D-\operatorname{per}F=\Omega(D),
$$

$$
\operatorname{area}(K\setminus F)=\Omega(D^2),
$$

$$
Z_{ext}=\Theta(D^2),
\qquad
Z_{ext}
=\frac2{\sqrt3}\operatorname{area}(K\setminus F)+O(D),
$$

and

$$
1<s_{ext}\le1+O(D^{-1}).
$$

This is stronger than the old ER dichotomy.  ER allowed either a near-isodiametric
force hull or a quadratic external population.  MP excludes the near-isodiametric
force-hull branch throughout `lambda<lambda_disk`, and AS identifies the surviving
population as an annular packing that is asymptotically density-saturated.

It still does not prove

$$
b+Q>2h
$$

or construct a strict sub-`D` competitor.  The missing information is now microscopic:
one must convert `O(D)` total annular packing defect, together with strict noncontact
and the fixed force-visible core, into a cardinality-preserving finite rearrangement or
an exact surplus charge.

---

## 7. Exact remaining lemma

The next closing theorem should target the saturation scale exposed by AS, rather than
another macroscopic area estimate.

> **ASR — saturated-annulus release.**  Fix `lambda_0<lambda_disk`.  For a post-ZF
> survivor in the AS.2 regime, use
> 

$$

> Z_{ext}=\frac2{\sqrt3}A_{ann}+O(D),
> \qquad
> s_{ext}=1+O(D^{-1}),
> 
$$


> together with the fixed force-visible core to construct an `n`-point unit-separated
> set of diameter `<D`, or prove an exact boundary surplus that implies
> `b+Q>2h`.
>
> The construction must preserve all `n` points.  It may not replace the annular
> population by an asymptotic density statement without controlling the `O(D)`
> boundary loss.

This is exactly where global optimality enters beyond the odd-shell regressions: ER's
lower population is tied to the strict `D(n)` lattice comparison, while AV supplies a
matching finite annular capacity upper bound.  Dense artificial shell fillings can
mimic the asymptotic geometry but do not carry that global-optimality lower bound.

---

## 8. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell without filling | yes | it has no quadratic external annulus population and lies outside the low-surplus branch because `e_BB/D->pi` |
| dense isolated shell filling | yes | it can mimic AS.12 geometrically, which is why ASR must use global finite capacity rather than density alone; no global-optimality certificate is inferred |
| FS odd-shell response trace | yes | AS uses neither response trace nor matching weight |
| contact-isolated points with gaps tending to one | yes | AS.3 permits exactly this; it does not assert a uniform separation gap |
| RA rattler absorption | yes | RA changes the contact representative and need not preserve `C=C_*`, `H=H_*`, or ZF; AS is stated only for the lexicographic source |

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| whole-source `delta_K=O(D)` | already implied / rederived | Oler nonnegativity plus exact strict full-source allowance |
| AV Voronoi constant | audited literature dependency | exact `2sqrt(3)` unit-disk Voronoi minimum; scales to `sqrt(3)/2` |
| AS.7 two-sided annular squeeze | proved | ER lower plus AV upper |
| AS.8 `Z_ext=(2/sqrt3)A_ann+O(D)` | proved | perimeter--diameter bounds |
| AS.2 low-surplus quadratic annulus | proved | MP + isoperimetry + whole-source area saturation |
| AS.3 `s_ext=1+O(1/D)` | proved | scaled AV compared with AS.4 |
| saturated annulus gives a strict competitor | not proved | requires ASR finite rearrangement at boundary-order accuracy |
| Level I | still open | high-surplus branch and ASR remain |

---

## 10. Canonical promotion recommendation

**Hold as report pending independent audit.**

AS.1--AS.3 depend on the report-level MP and AV/ER chain.  If that chain is promoted,
AS should replace the vague low-surplus phrase "quadratic isolated population" by the
stronger saturated-annulus normal form.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

AS annulus theorem:
Let A_ann=area(K)-area(F) and Z_ext be the external contact-isolated source points.
ER + AV give exactly
    (2/sqrt3)A_ann - per(F)/2 < Z_ext
and
    Z_ext <= (2/sqrt3)(A_ann+per(K)+per(F)+pi).
Hence
    Z_ext=(2/sqrt3)A_ann+O(D).

MP consequence:
For every lambda_0<lambda_disk=0.693272542288314..., low-surplus survivors have
    per(F) <= (pi-epsilon)D.
Isoperimetry plus whole-source delta_K=O(D) then gives
    A_ann=Omega(D^2),
    Z_ext=Theta(D^2),
and therefore
    Z_ext/A_ann -> 2/sqrt3.
Scaling AV by the external minimum separation gives
    s_ext=1+O(1/D),
while contact isolation keeps s_ext>1.

Exact next obligation ASR:
turn this O(D)-defect annular near-packing, with the fixed force-visible core, into a
strict sub-D n-point competitor or an exact boundary surplus implying b+Q>2h.
```
