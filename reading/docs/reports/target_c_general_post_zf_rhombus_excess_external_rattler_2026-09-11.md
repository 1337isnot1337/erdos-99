> Generated reading edition · [exact source](../../../docs/reports/target_c_general_post_zf_rhombus_excess_external_rattler_2026-09-11.md) · source SHA-256 `90cc25220efe337a115a208b8323bcfbc7eef9a6fa332a5096c36ebc8f5c0967`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-74773F99EE3C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_general_post_zf_rhombus_excess_external_rattler_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=88ab6ccb3fc83331544540b69425e682afe76db2; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — general post-ZF rhombus-excess / external-rattler transport

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact all-topology source-capacity identity  
**Target:** Target C, C-II after ZF  
**Depends on:** ZE/ZT post-ZF face identity, C51 convex bounded faces, OP internal outer-pocket absorption, strict translated-lattice comparison  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

The cyclic CRE report retained the positive area excess of every strict unit-rhombus
face, but stated its cancellation only in the `s_Z=d_H=0` Woodall cyclic branch.  The
same cancellation in fact holds for **every** post-ZF topology.  The full
`d_H+s_Z` defect cancels exactly.

Let

$$
a_0=\frac{\sqrt3}{2},
\qquad
c_0=\frac{\sqrt3}{4},
$$

and let `F` be the force hull.  If `N_F` is the entire source population lying in `F`,
including every contact-isolated point there, and

$$
E:=\sum_{R\text{ bounded quadrilateral face}}
\left(\operatorname{area}R-a_0\right)\ge0,
$$

then every post-ZF survivor satisfies

$$
\boxed{
a_0N_F
\le
\operatorname{area}F+c_0\operatorname{per}F+a_0-E.
}
\tag{GR.1}
$$

If `Z_ext=n-N_F` and

$$
\delta_F:=\frac{\pi D^2}{4}-\operatorname{area}F\ge0,
$$

then the strict global lattice comparison gives

$$
\boxed{
E+\delta_F
<
a_0Z_{ext}+c_0\operatorname{per}F.
}
\tag{GR.2}
$$

Thus external fully inactive source points are exactly the obstruction preventing the
cyclic boundary-order rhombus-defect transport from extending automatically to the
general post-ZF source.

---

## 1. General post-ZF face identity

Use the audited post-ZF notation

- `m=|V(C)|` for the nonisolated contact core;
- `q=|B_+|` for loaded force-hull vertices;
- `h=|E(H)|` for the full actual diameter graph;
- `d_H=q-h`;
- `s_Z=e+h-(2m-2)`;
- `k=d_H+s_Z`;
- `b` for the outer contact-face boundary-walk length;
- `R_4` for the number of bounded quadrilateral contact faces;
- `f` for the number of bounded nonquadrilateral faces;
- `Q=sum_F(deg F-4)` over those exceptional faces.

ZE gives exactly

$$
\boxed{b+Q=2(h-s_Z)=2(q-k).}
\tag{1.1}
$$

Euler and face incidence give in every connected plane contact core

$$
2m=2R_4+2f+b+Q+2.
\tag{1.2}
$$

Insert (1.1):

$$
\boxed{m=R_4+f+q-k+1.}
\tag{1.3}
$$

The cyclic CRE identity is the special case `k=0`; no cyclic topology is needed for
(1.3).

---

## 2. Oler on exceptional bounded faces

Let the exceptional faces be `F_i`, with

$$
r_i:=\deg(F_i)-4\ge1,
\qquad
\sum_i r_i=Q.
$$

Let `z_i` be the number of contact-isolated source points in the interior of `F_i`.
C51 makes every bounded contact face a strict convex unit-edge polygon, so Oler applies
to its boundary vertices together with those `z_i` points:

$$
a_0(4+r_i+z_i-1)
\le
\operatorname{area}(F_i)+c_0(4+r_i).
$$

Since `a_0=2c_0`, this is

$$
\boxed{
\operatorname{area}(F_i)
\ge a_0z_i+a_0+c_0r_i.
}
\tag{2.1}
$$

Put

$$
Z_{def}:=\sum_i z_i,
\qquad
A_{exc}:=\sum_i\operatorname{area}(F_i).
$$

Summing gives

$$
\boxed{A_{exc}\ge a_0(Z_{def}+f)+c_0Q.}
\tag{2.2}
$$

Every bounded quadrilateral is a strict unit rhombus, so if `A_4` is their total
area,

$$
\boxed{A_4=a_0R_4+E.}
\tag{2.3}
$$

Let

$$
A_{bnd}=A_4+A_{exc}.
$$

Use (1.3), (2.2), and (2.3):

$$
\begin{aligned}
a_0(m+Z_{def})
&=a_0R_4+a_0(f+Z_{def})+a_0(q-k)+a_0\\
&\le A_4-E+A_{exc}-c_0Q+a_0(q-k)+a_0\\
&=A_{bnd}-E-c_0Q+a_0(q-k)+a_0.
\end{aligned}
\tag{2.4}
$$

---

## 3. Add every isolated source point inside the force hull

Let `Z_in` be the contact-isolated source points lying in `F` but in the outer contact
face, and put

$$
H_{out}:=\operatorname{area}F-A_{bnd}.
$$

The general OP theorem, with no cyclic assumption, gives

$$
Z_{in}
\le
\frac1{a_0}H_{out}
+\frac{\operatorname{per}F-b}{2}.
$$

Multiplying by `a_0` and using `a_0/2=c_0`,

$$
\boxed{
a_0Z_{in}
\le H_{out}+c_0(\operatorname{per}F-b).
}
\tag{3.1}
$$

Add (3.1) to (2.4).  The complete source population inside `F` is

$$
N_F=m+Z_{def}+Z_{in}.
$$

Therefore

$$
\begin{aligned}
a_0N_F
&\le
\operatorname{area}F-E
-c_0(Q+b)
+a_0(q-k)
+c_0\operatorname{per}F+a_0.
\end{aligned}
\tag{3.2}
$$

Now use the exact general post-ZF identity (1.1):

$$
-c_0(Q+b)+a_0(q-k)
=-2c_0(q-k)+2c_0(q-k)=0.
$$

Hence

$$
\boxed{
a_0N_F
\le
\operatorname{area}F+c_0\operatorname{per}F+a_0-E.
}
$$

This proves GR.1.

The cancellation is the point: neither `d_H` nor `s_Z` leaves a remainder.

---

## 4. External-rattler / isodiametric-defect inequality

Let

$$
Z_{ext}:=n-N_F.
$$

The unconditional strict translated-lattice comparison for a global minimizer is

$$
\boxed{
a_0(n-1)>\frac{\pi D^2}{4}.}
\tag{4.1}
$$

GR.1 gives

$$
a_0n
\le
\operatorname{area}F+c_0\operatorname{per}F+a_0-E+a_0Z_{ext}.
$$

Subtract `a_0` and compare with (4.1):

$$
\frac{\pi D^2}{4}
<
\operatorname{area}F+c_0\operatorname{per}F-E+a_0Z_{ext}.
$$

Rearrangement proves

### Theorem GR — general rhombus-excess transport

$$
\boxed{
E+\left(\frac{\pi D^2}{4}-\operatorname{area}F\right)
<
\frac{\sqrt3}{2}Z_{ext}
+rac{\sqrt3}{4}\operatorname{per}F.
}
\tag{GR.3}
$$

Since `per(F)<=pi D`,

$$
\boxed{E+\delta_F<a_0Z_{ext}+\frac{\pi\sqrt3}{4}D.}
\tag{GR.4}
$$

---

## 5. Consequences

### Corollary GR.1 — subquadratic external population forces both defects subquadratic

If

$$
Z_{ext}=o(D^2),
$$

then

$$
\boxed{
\delta_F=o(D^2),
\qquad
E=o(D^2).
}
\tag{5.1}
$$

Both terms are nonnegative and GR.4 has right side `o(D^2)`.

Thus the old ER implication

$$
Z_{ext}=o(D^2)\Longrightarrow \operatorname{area}F/D^2\to\pi/4
$$

strengthens to simultaneous near-isodiametricity **and** vanishing normalized rhombus
angular-area defect.

### Corollary GR.2 — boundary-order external population recovers cyclic-strength defect transport

If

$$
Z_{ext}=O(D),
$$

then

$$
\boxed{E+\delta_F=O(D).}
\tag{5.2}
$$

In particular a post-ZF representative with `Z_ext=0` has boundary-order total strict
rhombus excess in every diameter topology, not only the cyclic Woodall branch.

### Corollary GR.3 — fixed force-hull area deficit requires external population or rhombus defect

For every `eta>0`, if

$$
\operatorname{area}F
\le\left(\frac\pi4-\eta\right)D^2,
$$

then

$$
\boxed{
Z_{ext}
>
\frac{2}{\sqrt3}\left(\eta D^2+E-c_0\operatorname{per}F\right).
}
\tag{5.3}
$$

The positive `E` term is absent from the previous external-rattler lower bound.

---

## 6. Exact remaining obstruction

GR does **not** prove `Z_ext=o(D^2)` for the C65 representative.  C65 says every point
outside the positive contact core is fully inactive, and ER/RA show that a quadratic
external population is a genuine representative-level escape.  RA can move those
points to first contact while keeping `n,D` and the original core fixed, but the new
contacts need not be KKT-positive, so the post-ZF identities cannot simply be
reapplied to the contact-richer representative.

Therefore the all-topology rhombus transport reduces the missing source-capacity step
to one explicit issue:

> prove a source-specific bound `Z_ext=o(D^2)` (ideally `O(D)`) for the
> contact/diameter-lexicographically minimal C65 representative, or prove a transfer
> theorem carrying the post-ZF force/stress geometry to the RA rattler-free
> representative.

No arbitrary annular Oler theorem is assumed.  Subtracting Oler inequalities for two
nested convex bodies does not justify such a result because a decomposition of the
annulus may create uncontrolled cut perimeter.

---

## 7. Regressions

- **Regular odd shell plus dense isolated filling:** GR permits the isolated population
  to pay the force-hull area deficit; it is not falsely excluded.
- **Heptagon plus center:** the center is an internal inactive point, so it is already
  included in `N_F`; GR reduces to a finite Oler inequality and remains valid.
- **Cyclic Woodall branch:** the Reuleaux cap theorem separately controls every source
  point outside `F`, recovering the stronger cyclic CRE estimate.  GR is the general
  precursor, not a replacement for that cap geometry.
- **`s_Z>0`:** retained exactly through (1.1); no circuit identity is used.
- **Forest diameter topology:** retained exactly through `d_H`; no caterpillar
  component is discarded.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For every post-ZF survivor, with k=d_H+s_Z,
    b+Q=2(q-k),
    m=R_4+f+q-k+1.
Write A_4=a0 R_4+E, where E>=0 is total strict-rhombus area excess.
Oler on exceptional bounded faces gives
    A_exc>=a0(Z_def+f)+c0 Q.
The general OP theorem gives
    a0 Z_in<=H_out+c0(P_F-b).
Adding these inequalities cancels the complete term
    -c0(Q+b)+a0(q-k)=0.
Hence for the entire source population N_F inside the force hull,
    a0 N_F<=area(F)+c0 P_F+a0-E.

With Z_ext=n-N_F and the strict global lattice comparison,
    E+[pi D^2/4-area(F)] < a0 Z_ext+c0 P_F.
Therefore
    Z_ext=o(D^2) => area(F)/D^2->pi/4 and E=o(D^2),
    Z_ext=O(D)   => isodiametric deficit + E = O(D).

The remaining obstruction is exactly a quadratic external-rattler population or a
representative-transfer theorem; d_H and s_Z themselves leave no remainder in the
rhombus-excess cancellation.
```
