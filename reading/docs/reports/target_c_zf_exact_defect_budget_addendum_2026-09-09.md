> Generated reading edition · [exact source](../../../docs/reports/target_c_zf_exact_defect_budget_addendum_2026-09-09.md) · source SHA-256 `e206f0ce98084cfa0ef63e7160456f9416cde4f587cb3efefb083c4ffb41f039`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-28C441DE9FE1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — exact post-ZF defect and boundary-surplus ledger

**Date:** 2026-09-09  
**Repository state:** `a8efd00fa7fca0c4a20911e86efd46cb0aadeb9c`  
**Run type:** exact closing-endpoint refinement  
**Target:** Target C, C-II after ZS  
**Depends on:** ZF, ZS, DT, C33, C42/C51, planar diameter-graph structure  
**External web search:** no theorem imported  
**Computation:** not used

The preceding ZS report proves that every audited post-ZF survivor lies in the linear boundary-surplus phase. This addendum resolves that undifferentiated surplus into exact nonnegative integer currencies. It derives:

1. an exact train/diameter/row-surplus ledger;
2. an exact partition of the loaded-terminal count by face and diameter defects;
3. an exact pinned-contact trichotomy showing where the linear boundary surplus must physically/combinatorially appear.

The Level I problem remains open. These are exact finite identities and branch reductions, not the missing strict inequality.

---

## 1. Starting notation

Use the notation of the ZS report:

- `v`: nonisolated contact-core vertices;
- `e`: unit-contact edges;
- `h`: actual diameter pairs;
- `q=|B_+|`: actual diameter endpoints;
- `delta`: contact-graph diameter.

ZS defines

$$
r_E:=2v-\delta-2-e\ge0,
\qquad
s_Z:=e+h-(2v-2)\ge0,
\tag{1.1}
$$

and proves

$$
\boxed{h=\delta+r_E+s_Z.}
\tag{1.2}
$$

Define

$$
\boxed{d_H:=q-h\ge0.}
\tag{1.3}
$$

For the connected plane contact core let

- `b` be the outer-face boundary-walk length, counted with multiplicity;
- `f` be the number of bounded nonquadrilateral faces;
- `Q=sum_F(deg(F)-4)` over bounded nonquadrilateral faces;
- `T` be the DT stopped-train count.

C42/C51 give

$$
\boxed{b\ge q,}
\tag{1.4}
$$

and every bounded nonquadrilateral face has degree at least five. DT gives

$$
\boxed{
T=\frac{b+Q}{2}+2f.
}
\tag{1.5}
$$

The campaign's remaining scalar closing inequality is

$$
\boxed{b+Q>2h.}
\tag{1.6}
$$

---

## 2. Theorem ZE — exact post-ZF defect ledger

Every post-ZF survivor satisfies

$$
\boxed{
q-\delta=d_H+r_E+s_Z,
}
\tag{ZE.1}
$$

$$
\boxed{
\sigma_B=2q-\delta-2
=q-2+d_H+r_E+s_Z,
}
\tag{ZE.2}
$$

and, wherever DT applies,

$$
\boxed{
2f=(T-q)+d_H+s_Z.
}
\tag{ZE.3}
$$

Equivalently,

$$
\boxed{s_Z=2f-(T-q+d_H).}
\tag{ZE.4}
$$

### Proof

By definition,

$$
q-\delta=(q-h)+(h-\delta).
$$

The first term is `d_H`; (1.2) gives `h-delta=r_E+s_Z`. This proves ZE.1. Then

$$
\sigma_B=q+(q-\delta)-2
$$

gives ZE.2.

Euler and face incidence give

$$
\boxed{
e=2v-2-\frac{b+Q}{2}.}
\tag{ZE.5}
$$

Hence

$$
\boxed{
s_Z=h-\frac{b+Q}{2},}
\qquad
\boxed{
\frac{b+Q}{2}=h-s_Z.
}
\tag{ZE.6}
$$

Substitute this into DT:

$$
T=h-s_Z+2f.
$$

Thus

$$
2f=T-h+s_Z=(T-q)+(q-h)+s_Z,
$$

which is ZE.3. ZE.4 is a rearrangement. `square`

---

## 3. Theorem ZT — exact terminal-defect partition

Define

$$
\boxed{x_B:=b-q\ge0}
\tag{ZT.1}
$$

and

$$
\boxed{
g_F:=Q-f
=\sum_{F\text{ exceptional}}(\deg F-5)\ge0.}
\tag{ZT.2}
$$

Then

$$
\boxed{
q=x_B+f+g_F+2d_H+2s_Z.
}
\tag{ZT.3}
$$

Consequently

$$
\boxed{f=q-x_B-g_F-2d_H-2s_Z,}
\tag{ZT.4}
$$

$$
\boxed{f\le q-2d_H-2s_Z,}
\tag{ZT.5}
$$

$$
\boxed{d_H+s_Z\le q/2,}
\tag{ZT.6}
$$

and

$$
\boxed{
T-q=2q-2x_B-2g_F-5(d_H+s_Z).
}
\tag{ZT.7}
$$

### Proof

Every exceptional bounded face has degree at least five, so

$$
Q=f+g_F.
$$

Also `b=q+x_B`. Thus

$$
b+Q=q+x_B+f+g_F.
\tag{ZT.8}
$$

ZE.6 and `h=q-d_H` give

$$
b+Q=2q-2d_H-2s_Z.
\tag{ZT.9}
$$

Equating ZT.8 and ZT.9 proves ZT.3. ZT.4–ZT.6 follow by rearrangement and nonnegativity. Finally ZE.3 gives

$$
T-q=2f-d_H-s_Z,
$$

and substitution of ZT.4 proves ZT.7. `square`

### Five terminal currencies

ZT.3 partitions the `q` loaded terminals exactly into:

1. `x_B`: repeated/excess outer-face walk beyond one appearance per loaded hull vertex;
2. `f`: one unit for each bounded nonquadrilateral face;
3. `g_F`: additional face-degree excess above pentagons;
4. `2d_H`: two units per diameter-graph tree-component deficit;
5. `2s_Z`: two units per extra mixed-framework row dependency.

No `O(D)` remainder remains in this bookkeeping.

---

## 4. Theorem ZU — exact pinned-contact surplus trichotomy

Let

- `I=V(C)\setminus B_+`;
- `c_I` be the number of connected components of `C[I]`;
- `e_BB` be the number of unit contacts with both endpoints in `B_+`.

C33 proves

$$
e-e_{BB}\ge2(v-q)+c_I.
$$

Define its exact nonnegative slack

$$
\boxed{
s_C:=(e-e_{BB})-2(v-q)-c_I\ge0.}
\tag{ZU.1}
$$

Then every post-ZF survivor satisfies

$$
\boxed{
c_I+e_{BB}+s_C=q-2+d_H+s_Z.}
\tag{ZU.2}
$$

In particular,

$$
\boxed{
c_I+e_{BB}+s_C\ge q-2\ge\lceil D\rceil-2,}
\tag{ZU.3}
$$

so at least one of the three quantities obeys

$$
\boxed{
\max\{c_I,e_{BB},s_C\}
\ge
\frac{q-2+d_H+s_Z}{3}
\ge
\frac{\lceil D\rceil-2}{3}.
}
\tag{ZU.4}
$$

Combining ZU.2 with ZT.3 gives the dual exact balance

$$
\boxed{
 c_I+e_{BB}+s_C+2
 =x_B+f+g_F+3(d_H+s_Z).
}
\tag{ZU.5}
$$

### Proof

By definition of `s_C`,

$$
e=2v-2q+c_I+e_{BB}+s_C.
\tag{ZU.6}
$$

Therefore

$$
\begin{aligned}
r_E
&=2v-\delta-2-e\\
&=2q-\delta-2-c_I-e_{BB}-s_C\\
&=\sigma_B-c_I-e_{BB}-s_C.
\end{aligned}
\tag{ZU.7}
$$

ZE.2 gives

$$
\sigma_B=q-2+d_H+r_E+s_Z.
$$

Insert this in ZU.7 and cancel `r_E` from both sides:

$$
0=q-2+d_H+s_Z-c_I-e_{BB}-s_C.
$$

This proves ZU.2. ZU.3 follows from nonnegativity of `d_H,s_Z` and `q>=h>=delta>=ceil(D)`. ZU.4 is pigeonhole. Finally substitute

$$
q=x_B+f+g_F+2(d_H+s_Z)
$$

from ZT.3 into ZU.2, which gives ZU.5. `square`

### Interpretation of `s_C`

C33 pins every loaded terminal. The pinned contact rigidity matrix is block diagonal over the `c_I` interior components, and each block has full column rank `2|I_r|`. Therefore the total pinned-contact left-nullity is

$$
(e-e_{BB})-2(v-q)=c_I+s_C.
\tag{ZU.8}
$$

C33's positive KKT stress supplies one mandatory nonzero left-kernel vector on each interior component. Hence

$$
\boxed{
s_C=\text{the number of additional pinned-contact left-kernel dimensions beyond those }c_I\text{ mandatory ones}.}
\tag{ZU.9}
$$

Thus ZU is not merely a reparameterization of `sigma_B`: it says the post-ZF linear boundary surplus must materialize as a linear number of interior components, direct loaded-loaded contacts, or extra pinned-contact stress dependencies.

---

## 5. Structural interpretations of `d_H` and `s_Z`

The canonical planar diameter-graph structure says each component is a caterpillar whose spine is a path or one odd cycle, with at most one unicyclic component. Therefore

$$
\boxed{d_H=q-h=\text{number of tree components of }H.}
\tag{5.1}
$$

ZF gives mixed active rigidity rank `2v-3`, so its left-nullity is

$$
(e+h)-(2v-3)=s_Z+1.
\tag{5.2}
$$

The mandatory KKT dependence accounts for one dimension. Hence

$$
\boxed{s_Z=\text{extra mixed-framework row dependencies beyond the mandatory KKT dependence}.}
\tag{5.3}
$$

So ZT/ZU track two different stress redundancies: `s_C` before matching boundary reactions to the diameter system, and `s_Z` after the full contact/diameter equilibrium constraints are imposed.

---

## 6. Exact closing form

The desired face inequality

$$
b+Q>2h
$$

is, by ZE.6, equivalent to

$$
s_Z<0,
$$

which contradicts ZF.

In stopped-train variables it is equivalent to

$$
\boxed{T-q+d_H>2f,}
\tag{6.1}
$$

or by integrality

$$
\boxed{T-q+d_H\ge2f+1.}
\tag{6.2}
$$

ZE.3 identifies the exact survivor obstruction:

$$
\boxed{T-q+d_H=2f-s_Z\le2f.}
\tag{6.3}
$$

ZT.7 gives the corresponding exact terminal-budget expression

$$
\boxed{T-q=2q-2x_B-2g_F-5(d_H+s_Z).}
\tag{6.4}
$$

A closing theorem must therefore add genuinely new geometric/global-optimality information; the exact linear ledger itself cannot change the sign of `s_Z`.

---

## 7. Dense-core consequences

Let

$$
\Delta=\frac{\pi}{2\sqrt3},
\qquad
c_0:=2\sqrt\Delta-\frac\pi2
=0.333829286933018\ldots.
\tag{7.1}
$$

Under the existing DE/DF hypothesis

$$
n-v=o(D^2),
\tag{7.2}
$$

the reviewed train theorem gives

$$
\liminf\frac{T-q}{D}\ge c_0.
\tag{7.3}
$$

ZE.3 then gives

$$
\boxed{
\liminf
\frac{f-(d_H+s_Z)/2}{D}
\ge
\sqrt\Delta-\frac\pi4
=0.166914643466509\ldots.
}
\tag{7.4}
$$

Using ZT.7 also gives

$$
\boxed{
\limsup
\frac{2x_B+2g_F+5(d_H+s_Z)}{D}
\le
2\limsup\frac qD-c_0.
}
\tag{7.5}
$$

and hence, from `q<=pi D`,

$$
\boxed{
\limsup
\frac{2x_B+2g_F+5(d_H+s_Z)}{D}
\le
2\pi-c_0.
}
\tag{7.6}
$$

The useful content is structural: a dense-core sequence near the exposed-hull train lower bound cannot simultaneously spend a linear terminal budget on outer repetition, high-degree exceptional faces, diameter tree components, and extra mixed dependencies.

No statement here removes the population hypothesis (7.2).

---

## 8. Regression audit

### Regular odd contact shell

For a regular unit odd `q`-gon with the contact graph equal to the boundary cycle:

- `x_B=0`;
- one bounded exceptional `q`-gon gives `f=1`, `g_F=q-5`;
- the diameter graph is one odd unicyclic component, so `d_H=0`;
- `v=e=h=q`, so `s_Z=2`;
- all vertices are loaded, so `c_I=0`, `e_BB=q`, `s_C=0`.

ZT.3 gives

$$
0+1+(q-5)+0+4=q,
$$

and ZU.2 gives

$$
0+q+0=q-2+0+2.
$$

Both are exact. Thus the new identities correctly retain the regular-shell regression instead of deriving a false topological contradiction.

### Unit square

Here `q=4`, the diameter graph is a two-edge matching, so `d_H=2`, while `s_Z=0`. All contacts are loaded-loaded: `e_BB=4`, `c_I=s_C=0`. ZU.2 reads `4=4-2+2`, again exactly.

### Crossing diameter matching

Every matching component is a tree, so `d_H` may be large. The ledger charges it exactly and never uncrosses the matching or replaces it by a star.

### Strict pentagonal exceptional face

A strict pentagon has `g_F=0`. ZT assigns only the one face-count unit and no uniform Oler surplus. DP remains binding.

### Regular heptagon plus isolated center

No contact-isolated source point is counted in `v`, and no isolate is declared diametral. The rejected force-bulk argument is not revived.

### Bridges and articulation

Outer-face walk multiplicity is retained in `x_B`. C51 puts bridges only on the outer face and keeps bounded faces simple, so bridge complexity is charged rather than silently discarded.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| Z/ZC/ZR/ZF/ZB | reviewed report-level results | Status unchanged from the September 9 consolidated audit. |
| ZS boundary-surplus collapse | proved in preceding report | Supplies the post-ZF source class and (1.2). |
| ZE.1–ZE.4 | proved and new | Exact algebra plus Euler and DT. |
| ZT.3 terminal-defect partition | proved and new | C42/C51 plus ZE.6. |
| ZU.2 pinned-surplus trichotomy | proved and new | C33 slack identity plus ZE.2. |
| `d_H` tree-component interpretation | correct but canonical | Existing planar diameter pseudoforest theorem. |
| `s_Z`, `s_C` left-nullity interpretations | proved | Rank-nullity applied to the mixed and pinned rigidity matrices. |
| dense-core refinements | proved conditionally | Retain `n-v=o(D^2)`. |

---

## 10. Failed implications / no-go results

1. Large `sigma_B` does not by itself force `c_I` or `e_BB` large; ZU shows a third branch `s_C` can absorb the surplus.
2. A linear `s_C` is not automatically a full KKT stress-space dimension; pinned contact stresses may induce boundary reactions not realizable by diameter coefficients.
3. Many off-star diameter edges do not imply positive off-star `beta` mass; relative-interior positivity has no uniform floor.
4. ZT is not a face-local Oler charge; DP still rules out a universal positive surplus per exceptional face.
5. No isolate-control theorem is obtained.
6. The identities themselves cannot prove the strict closing sign. A new source-specific geometric/global-optimality theorem remains necessary.

---

## 11. Promotion recommendation

**Hold as report.**

The deductions are exact, but ZF remains report-level. If the Z stack is promoted, update the post-ZF Target C frontier with:

- `sigma_B=q-2+d_H+r_E+s_Z`;
- `q=x_B+f+g_F+2d_H+2s_Z`;
- `c_I+e_BB+s_C=q-2+d_H+s_Z`;
- `2f=(T-q)+d_H+s_Z`;
- the explicit statement that C44's `sigma_B=o(D)` alternatives are pre-ZF only.

Do not promote these consequences independently of their ZF dependency.

---

## 12. Highest-value next branch split

The exact closing theorem remains

$$
\boxed{T-q+d_H\ge2f+1.}
\tag{12.1}
$$

The new ledgers reduce the post-ZF general topology to explicit currencies.

### A. Many interior components

If `c_I>= (q-2+d_H+s_Z)/3`, use C36–C40 noncrossing attachment incidence and component diameter cost without assuming `sigma_B=o(D)`. The target is a global capacity contradiction for a linear number of distinct harmonic components.

### B. Many loaded-loaded contacts

If `e_BB` is linear, exploit convex-hull order, unit separation, loaded contact degree at most three, and C18 diameter-direction restrictions. The target is an exact boundary-length/diameter contradiction or forced face surplus.

### C. Large pinned-contact stress surplus

If `s_C` is linear, the pinned contact network has linearly many extra equilibrium-stress dimensions beyond the mandatory one per interior component. The live linear-algebra question is whether enough of these boundary-reaction directions must intersect the diameter-reaction subspace to force either larger `s_Z`, a nonzero response defect, or a finite release contradicting lexicographic minimality.

Independently, ZT splits the face topology into `x_B`, `f`, `g_F`, and `d_H+s_Z`. A proof can now target the large currency rather than treating all exceptional topology as one `O(D)` remainder.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Post-ZF exact slacks:
    r_E = 2v-delta-2-e,
    s_Z = e+h-(2v-2),
    d_H = q-h.
Then
    q-delta = d_H+r_E+s_Z,
    sigma_B = q-2+d_H+r_E+s_Z,
    2f = (T-q)+d_H+s_Z.

Exact terminal partition:
    x_B = b-q >=0,
    g_F = sum_exc(deg F-5) >=0,
    q = x_B+f+g_F+2d_H+2s_Z.
Hence
    f <= q-2d_H-2s_Z,
    d_H+s_Z <= q/2,
    T-q = 2q-2x_B-2g_F-5(d_H+s_Z).

Exact pinned-contact trichotomy:
    s_C=(e-e_BB)-2(v-q)-c_I >=0,
    c_I+e_BB+s_C = q-2+d_H+s_Z >= ceil(D)-2.
Thus at least one of c_I, e_BB, s_C is >=(ceil(D)-2)/3.
Also
    c_I+e_BB+s_C+2
      = x_B+f+g_F+3(d_H+s_Z).

Interpretation:
- d_H = number of diameter-graph tree components;
- s_Z = extra full mixed-framework row dependencies beyond KKT;
- s_C = extra pinned-contact row dependencies beyond one per interior component.

Dense-core refinement (still conditional on n-v=o(D^2)):
    liminf [f-(d_H+s_Z)/2]/D
      >= sqrt(pi/(2sqrt(3))) - pi/4
      = 0.166914643466509... .

Exact endpoint:
    T-q+d_H >= 2f+1.
A survivor instead satisfies
    T-q+d_H = 2f-s_Z.

New exact post-ZF trichotomy:
A. linearly many interior components;
B. linearly many loaded-loaded contacts;
C. linearly many extra pinned-contact stress dependencies.
```
