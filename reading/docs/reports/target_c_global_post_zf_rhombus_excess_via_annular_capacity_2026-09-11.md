> Generated reading edition · [exact source](../../../docs/reports/target_c_global_post_zf_rhombus_excess_via_annular_capacity_2026-09-11.md) · source SHA-256 `570e52616de915bab05e8ff5b95c4eadfb516bf658c84927094007d48dc9e0b9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9E075C4C0DEB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_global_post_zf_rhombus_excess_via_annular_capacity_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6e986801097377f1ab776f4719ea7578f8ebf430; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — global post-ZF rhombus-excess transport via annular capacity

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783` plus the preceding GR report on this branch  
**Run type:** exact theorem synthesis / all-topology phase transport  
**Target:** Target C, C-II after ZF  
**Depends on:** GR general inside-force-hull rhombus excess, AV annular Voronoi capacity, Cauchy perimeter bound  
**External input:** no new input; AV already imported and audited its Voronoi-cell theorem

## LEVEL I STATUS

`STILL OPEN`.

The preceding GR theorem proves for every post-ZF survivor

$$
E+\delta_F
< a_0 Z_{ext}+c_0P_F,
\qquad
a_0={\sqrt3\over2},\quad c_0={\sqrt3\over4},
\tag{1.1}
$$

where

- `E>=0` is total area excess of bounded strict unit-rhombus contact faces above
  `sqrt(3)/2` per face;
- `delta_F=pi D^2/4-area(F)>=0`;
- `Z_ext` is the unit-separated source population outside the force hull;
- `P_F=per(F)`.

At first sight a quadratic `Z_ext` appears to block any general `E=O(D)` conclusion.
The already-promoted annular Voronoi theorem AV has exactly the coefficient needed to
remove that obstruction.  If `K=conv(A)` is the full source hull, AV gives

$$
Z_{ext}
\le {2\over\sqrt3}
\bigl(area(K)-area(F)+P_K+P_F+\pi\bigr).
\tag{1.2}
$$

Since `a_0(2/sqrt3)=1`, substitution cancels the complete force-hull area deficit.
The result is an all-topology boundary-order rhombus-defect theorem:

$$
\boxed{
E<P_K+(1+c_0)P_F+\pi
\le \pi D\left(2+{\sqrt3\over4}\right)+\pi.
}
\tag{1.3}
$$

Thus every post-ZF survivor, including `s_Z>0`, every Woodall forest topology, every
external-rattler population, and every outer-pocket configuration, has only `O(D)`
total strict-rhombus angular-area defect.

This removes the cyclic hypothesis from the main CRE phase-transport conclusion.

---

## 1. Inputs

Let `F` be the force hull of the C65 post-ZF positive core and `K=conv(A)` the full
source hull.  Then

$$
F\subseteq K,
\qquad
\operatorname{diam}F=\operatorname{diam}K=D.
\tag{1.4}
$$

Let

$$
\delta_F={\pi D^2\over4}-area(F).
$$

The general rhombus-excess theorem GR on the present branch proves

$$
\boxed{E+\delta_F<a_0Z_{ext}+c_0P_F.}
\tag{1.5}
$$

The already-promoted annular Voronoi theorem AV applies to the external source points

$$
S=A\setminus F\subseteq K\setminus int(F),
$$

which remain unit-separated.  It gives

$$
\boxed{
a_0Z_{ext}
\le area(K)-area(F)+P_K+P_F+\pi.}
\tag{1.6}
$$

No contact, KKT, or triangle-free hypothesis enters AV beyond the unit separation of
this source subset.

---

## 2. Exact cancellation of the quadratic area deficit

Write

$$
\delta_K={\pi D^2\over4}-area(K)\ge0.
$$

Then

$$
area(K)-area(F)=\delta_F-\delta_K\le\delta_F.
\tag{2.1}
$$

Insert (1.6) into (1.5):

$$
\begin{aligned}
E+\delta_F
&< area(K)-area(F)+P_K+P_F+\pi+c_0P_F\\
&=\delta_F-\delta_K+P_K+(1+c_0)P_F+\pi.
\end{aligned}
$$

Cancel `delta_F` from both sides.  This proves the sharper finite form

### Theorem GA — global post-ZF rhombus excess

$$
\boxed{
E+\delta_K
< P_K+(1+c_0)P_F+\pi.
}
\tag{GA.1}
$$

In particular

$$
\boxed{
E<P_K+(1+c_0)P_F+\pi.
}
\tag{GA.2}
$$

Both `F` and `K` have diameter `D`.  Cauchy's perimeter-diameter inequality gives

$$
P_F,P_K\le\pi D.
$$

Therefore

$$
\boxed{
E
<\pi D\left(2+{\sqrt3\over4}\right)+\pi.
}
\tag{GA.3}
$$

The coefficient is explicit but is not claimed sharp.

A useful extra consequence of GA.1 is that the full source hull itself has only a
boundary-order isodiametric deficit whenever the rhombus excess is nonnegative:

$$
\boxed{
\delta_K<P_K+(1+c_0)P_F+\pi=O(D).
}
\tag{GA.4}
$$

Thus every post-ZF hypothetical counterexample has

$$
\boxed{
area(K)={\pi D^2\over4}-O(D).
}
\tag{GA.5}
$$

This conclusion is stronger than the previously used Bonnesen consequence
`area(K)=pi D^2/4-O(D)`: here it falls out of the same exact annular/rhombus ledger.
It is consistent with, and does not replace, the promoted full-source theorem FS.

---

## 3. Phase consequence

For a strict unit rhombus with acute angle

$$
\theta\in(\pi/3,\pi/2],
$$

its area excess is

$$
\sin\theta-\sqrt3/2.
$$

The promoted Target B phase-cut theorem PC applies to the actual finite family of
strict rhombic bounded faces without requiring that the whole C-II source be a pure
rhombic disk.  If `Delta_train` is the total train angular defect, PC gives

$$
{3\Delta_{train}\over\pi}
\le(2+\sqrt3)E.
\tag{3.1}
$$

GA.3 therefore yields

$$
\boxed{\Delta_{train}=O(D)}.
\tag{GA.6}
$$

Moreover PC deletes at most

$$
\left\lfloor{3\Delta_{train}\over\pi}\right\rfloor=O(D)
\tag{3.2}
$$

rhombus-crossing relations and leaves an exact acyclic real phase potential on the
remaining train graph.

Hence the boundary-order phase reduction previously obtained by CRE only in the
cyclic `s_Z=d_H=0` branch is now valid throughout the full post-ZF branch.

This does **not** assert a pure disk, first-order jamming, or that exceptional faces
and outer pockets disappear.  Trains are the stopped DT trains of the actual contact
core.

---

## 4. Why the cancellation was previously missed

GR alone gives

$$
E+\delta_F<a_0Z_{ext}+O(D)
$$

and therefore seems to leave a quadratic external-population escape.  ER similarly
records external rattlers as the residual force-bulk obstruction.

AV has coefficient `2/sqrt3`, exactly reciprocal to the Oler coefficient
`a_0=sqrt3/2`.  Consequently its leading annular area term is

$$
a_0Z_{ext}\le area(K)-area(F)+O(D),
$$

which is exactly the difference between the full-hull and force-hull isodiametric
deficits.  Substitution removes the unknown `delta_F` identically, rather than
estimating it.

No asymptotic density approximation is involved in this cancellation.

---

## 5. Scope and regressions

- **Quadratic external rattlers:** retained in the proof; AV absorbs them and they no
  longer obstruct `E=O(D)`.
- **`s_Z>0`:** fully retained because GR uses only the exact post-ZF identity
  `b+Q=2(q-d_H-s_Z)` and its `d_H+s_Z` terms cancel.
- **Caterpillar forest diameter support:** retained.
- **Cyclic Woodall support:** GA is compatible with CRE but has a weaker numerical
  coefficient because it uses only general annular capacity, not Reuleaux caps.
- **Exceptional bounded faces and outer pockets:** retained; GA controls rhombus area
  excess, not their total area or count.
- **Oblique rhombic grids:** still a binding geometric regression.  They can have
  `E=O(D)` and no unit triangles, so GA is not a Level I contradiction by itself.

---

## 6. New exact frontier

The general post-ZF C-II source now satisfies simultaneously:

```text
full source hull: area(K)=pi D^2/4-O(D)
actual strict-rhombus faces: total area/angular defect E=O(D)
Target B phase cut: only O(D) crossing relations need be removed
post-ZF mixed rigidity: full actual contact/diameter support retained
external source population: no longer an obstruction to the E=O(D) phase transport
```

The next useful theorem should therefore use this global boundary-order phase control
against the post-ZF rigidity circuit/dependency structure, rather than spending more
effort merely bounding external rattlers.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

GR (new on this branch):
    E+delta_F < a0 Z_ext+c0 P_F.
AV (already promoted):
    a0 Z_ext <= area(K)-area(F)+P_K+P_F+pi
               =delta_F-delta_K+P_K+P_F+pi.
Substitute and cancel delta_F exactly:
    E+delta_K < P_K+(1+c0)P_F+pi.
Hence
    E < pi D(2+sqrt3/4)+pi = O(D),
and also
    delta_K=O(D).

Therefore every post-ZF survivor, with arbitrary d_H, s_Z, exceptional faces,
outer pockets, and external rattlers, has boundary-order total rhombus angular defect.
Target B PC consequently deletes only O(D) rhombus-crossing relations and produces an
exact acyclic phase potential on the retained stopped-train graph.
```
